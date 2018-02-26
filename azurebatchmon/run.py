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

def run(args):

    start_time = datetime.datetime.now().replace(microsecond=0)
    print('Sample start: {}'.format(start_time))
    print()

    sample_list = [args.sample_name]
    fastq_container = [args.fastq_container]
    fastq1_list = [args.fastq1]
    fastq2_list = [args.fastq2]
    output_container_name = args.output_container

    # Create the blob client
    blob_client = azureblob.BlockBlobService(
        account_name=args.STORAGE_ACCOUNT_NAME,
        account_key=args.STORAGE_ACCOUNT_KEY)

    # Use the blob client to create the containers in Azure Storage if they
    # don't yet exist.
    blob_client.create_container(output_container_name, fail_on_exist=False)

    # Create a Batch service client.
    credentials = batchauth.SharedKeyCredentials(
        args.BATCH_ACCOUNT_NAME,
        args.BATCH_ACCOUNT_KEY)

    batch_client = batch.BatchServiceClient(
        credentials,
        base_url=args.BATCH_ACCOUNT_URL)

    # The resource files we pass in are used for configuring the pool's
    # start task, which is executed each time a node first joins the pool
    task_commands = ['sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common',
                     'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -',
                     'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"',
                     'sudo apt-get update',
                     'sudo apt-get install -y docker-ce']

    # Create the pool that will contain the compute nodes that will execute the
    # tasks.
    client_util.create_pool(batch_client,
        args.POOL_ID,
        args.NODE_OS_PUBLISHER,
        args.NODE_OS_OFFER,
        args.NODE_OS_SKU,
        args.POOL_VM_SIZE,
        args.POOL_NODE_COUNT,
        task_commands
    )

    # Create the job that will run the tasks.
    client_util.create_job(batch_client,
        args.JOB_ID,
        args.POOL_ID)

    # Get the strage file information.
    input_files1_resources = [
        client_util.get_resourcefile(blob_client, fastq_container[idx], fastq1_list[idx])
        for idx in range(len(fastq1_list))]
    input_files2_resources = [
        client_util.get_resourcefile(blob_client, fastq_container[idx], fastq2_list[idx])
        for idx in range(len(fastq2_list))]

    # get reference genome
    ref_container_name = args.REF_CONTAINER_NAME
    ref_file_paths = args.REF_FILE_PATH.split(",")
    ref_file_resources = [
        client_util.get_resourcefile(blob_client, ref_container_name, ref_file_path)
        for ref_file_path in ref_file_paths]

'''
    output_container_sas_token = \
        blob_client.generate_container_shared_access_signature(
            output_container_name,
            permission=azureblob.BlobPermissions.WRITE,
            expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=2))

    run_elevated = batchmodels.UserIdentity(
        auto_user=batchmodels.AutoUserSpecification(
        scope=batchmodels.AutoUserScope.pool,
        elevation_level=batchmodels.ElevationLevel.admin,
        )
    )
 
    tasks = list()
    for idx in range(len(input_files1_resources)):

        command = ['docker pull ken01nn/azure_batch_bwa',
                   'docker run -v $PWD:/mnt ken01nn/azure_batch_bwa '
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
                       conf.get("client","STORAGE_ACCOUNT_NAME"),
                       output_container_name,
                       output_container_sas_token)]

        print('command: ' + command[1])

        r_files = [input_files1_resources[idx], input_files2_resources[idx]]
        r_files.extend(ref_file_resources)
        
        tasks.append(batch.models.TaskAddParameter(
                'topNtask{}'.format(idx),
                common.helpers.wrap_commands_in_shell('linux', command),
                resource_files=r_files,
                user_identity=run_elevated
                )
        )
  
    batch_client.task.add_collection(conf.get("batch","JOB_ID"), tasks)

    # Pause execution until tasks reach Completed state.
    client_util.wait_for_tasks_to_complete(batch_client,
               conf.get("batch","JOB_ID"),
               datetime.timedelta(minutes=int(conf.get("batch","TIME_OUT"))))

    print("  Success! All tasks reached the 'Completed' state within the "
          "specified timeout period.")

    # Print out some timing info
    end_time = datetime.datetime.now().replace(microsecond=0)
    print()
    print('Sample end: {}'.format(end_time))
    print('Elapsed time: {}'.format(end_time - start_time))

    pass
'''
