[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# azurebatchmon
Wrapper program for Azure Batch simple job submission

# Installation
```sh
pip install azurebatchmon
```

## Requirement
need Azure Storage account and Azure Batch account.

## Task File


## RUN
```sh
usage: azurebatchmon [-h] [--version] --image genomon/star_alignment:0.1.0 --tasks star-alignment-tasks.csv --script star_alignment.sh \
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
