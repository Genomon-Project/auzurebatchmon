[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# azurebatchmon
Wrapper program for Azure Batch simple job submission

# Installation

```sh
pip install azurebatchmon
```

# Command

```sh
usage: azurebatchmon [-h] [--version] --image IMAGE --tasks TASKS --script SCRIPT \
                     --APP_CONTAINER APP_CONTAINER \
                     --STORAGE_ACCOUNT_NAME STORAGE_ACCOUNT_NAME \
                     --STORAGE_ACCOUNT_KEY STORAGE_ACCOUNT_KEY \
                     --BATCH_ACCOUNT_NAME BATCH_ACCOUNT_NAME \
                     --BATCH_ACCOUNT_KEY BATCH_ACCOUNT_KEY \
                     --BATCH_ACCOUNT_URL BATCH_ACCOUNT_URL \
                     --POOL_ID pool_id_prefix \
                     --NODE_OS_PUBLISHER NODE_OS_PUBLISHER \
                     --NODE_OS_OFFER NODE_OS_OFFER \
                     --NODE_OS_SKU NODE_OS_SKU \
                     --POOL_VM_SIZE POOL_VM_SIZE \
                     --POOL_DEDICATED_NODE_COUNT POOL_DEDICATED_NODE_COUNT \
                     --POOL_LOW_PRIORITY_NODE_COUNT POOL_LOW_PRIORITY_NODE_COUNT \
                     --JOB_ID job_id_prefix
                     [--debug]
```

## Command sample code

```sh
usage: azurebatchmon [-h] [--version] --image genomon/star_alignment:0.1.0 --tasks task_file --script star_alignment.sh \
                     --APP_CONTAINER script \
                     --STORAGE_ACCOUNT_NAME ******** \
                     --STORAGE_ACCOUNT_KEY ******** \
                     --BATCH_ACCOUNT_NAME ******** \
                     --BATCH_ACCOUNT_KEY ******** \
                     --BATCH_ACCOUNT_URL ******** \
                     --POOL_ID StarAlignment \
                     --NODE_OS_PUBLISHER Canonical \
                     --NODE_OS_OFFER UbuntuServer  \
                     --NODE_OS_SKU 16   \
                     --POOL_VM_SIZE Standard_D16_v3 \
                     --POOL_DEDICATED_NODE_COUNT 12 \
                     --POOL_LOW_PRIORITY_NODE_COUNT 0  \
                     --JOB_ID StarAlignment
                     [--debug]
```


