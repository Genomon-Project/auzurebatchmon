#! /usr/bin/env python

from __future__ import print_function
import datetime
import os
import sys
import time
import client_util

import azure.storage.blob as azureblob
import azure.batch.batch_service_client as batch
import azure.batch.batch_auth as batchauth
import azure.batch.models as batchmodels
import common.helpers  # noqa

from task_parser import *
from command_maker import *

def run(args):

    start_time = datetime.datetime.now().replace(microsecond=0)
    print('Sample start: {}'.format(start_time))
    print()


    # Create a Batch service client.
    credentials = batchauth.SharedKeyCredentials(
        args.BATCH_ACCOUNT_NAME,
        args.BATCH_ACCOUNT_KEY)

    batch_client = batch.BatchServiceClient(
        credentials,
        base_url=args.BATCH_ACCOUNT_URL)

    # The resource files we pass in are used for configuring the pool's
    # start task, which is executed each time a node first joins the pool
    pool_start_commands = [
        'sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common',
        'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -',
        'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"',
        'sudo apt-get update',
        'sudo apt-get install -y docker-ce',
    ]

    # Create the pool that will contain the compute nodes that will execute the
    # tasks.
    client_util.create_pool(batch_client,
        args.POOL_ID,
        args.NODE_OS_PUBLISHER,
        args.NODE_OS_OFFER,
        args.NODE_OS_SKU,
        args.POOL_VM_SIZE,
        args.POOL_NODE_COUNT,
        pool_start_commands
    )

    # Create the job that will run the tasks.
    client_util.create_job(batch_client,
        args.JOB_ID,
        args.POOL_ID)

    run_elevated = batchmodels.UserIdentity(
        auto_user=batchmodels.AutoUserSpecification(
        scope=batchmodels.AutoUserScope.pool,
        elevation_level=batchmodels.ElevationLevel.admin,
        )
    )
 
    tasks = list()
    commands = list()
    in_tasks = parseTasksFile(args.task_file)
    for idx, task in enumerate(in_tasks):
        for input_key in task.inputs:
            commands.append(
                make_download(task.inputs[input_key], args.STORAGE_ACCOUNT_KEY, False)
            )
        for input_key in task.input_recursive:
            commands.append(
                make_download(task.input_recursive[input_key], args.STORAGE_ACCOUNT_KEY, True)
            )

        tasks.append(batch.models.TaskAddParameter(
                'azbatchmon_task{}'.format(idx),
                common.helpers.wrap_commands_in_shell('linux', commands),
                user_identity=run_elevated
                )
        )
    batch_client.task.add_collection(args.JOB_ID, tasks)

    # Pause execution until tasks reach Completed state.
    client_util.wait_for_tasks_to_complete(batch_client,
               args.JOB_ID,
               datetime.timedelta(minutes=int(120)))

    print("  Success! All tasks reached the 'Completed' state within the "
          "specified timeout period.")

    # Print out some timing info
    end_time = datetime.datetime.now().replace(microsecond=0)
    print()
    print('Sample end: {}'.format(end_time))
    print('Elapsed time: {}'.format(end_time - start_time))



'''           
        command = ['docker run -v $PWD:/mnt ken01nn/azure_batch_bwa '
                   'python /bin/python_bwa_task.py '
                   '--bwapath /bin/bwa-0.7.15/bwa '
                   '--refgenome {} --samplename {} '
                   '--fastq1 {} --fastq2 {} '
                   '--storageaccount {} '
                   '--storagecontainer {} '
                   '--sastoken "{}" '.format(
                       ref_file_resources[0].file_path,
                       sample_list[idx],
                       input_files1_resources[idx].file_path,
                       input_files2_resources[idx].file_path,
                       args.STORAGE_ACCOUNT_NAME,
                       output_container_name,
                       output_container_sas_token)]
        
        command2 = ['touch hogehoge']

        command3 = ['docker run -v $PWD:/mnt ken01nn/lifecycle azcopy '
                   '--source /mnt/hogehoge '
                   '--destination https://{}.blob.core.windows.net/{}/hogehoge '
                   '--dest-key {}'.format(
                       args.STORAGE_ACCOUNT_NAME,
                       args.output_container,
                       args.STORAGE_ACCOUNT_KEY)]

'''           
