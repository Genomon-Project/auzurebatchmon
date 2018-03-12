[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# azurebatchmon
Wrapper program for Azure Batch simple job submission

# Installation

```sh
git clone https://github.com/Genomon-Project/azurebatchmon.git
cd genomon_pipeline_cloud
pip install . --upgrade
```

# Quick Start

```sh
usage: azurebatchmon [-h] [--version] --image IMAGE --tasks TASKS --script SCRIPT \
                     --APP_CONTAINER APP_CONTAINER \
                     --STORAGE_ACCOUNT_NAME STORAGE_ACCOUNT_NAME \
                     --STORAGE_ACCOUNT_KEY STORAGE_ACCOUNT_KEY \
                     --BATCH_ACCOUNT_NAME BATCH_ACCOUNT_NAME \
                     --BATCH_ACCOUNT_KEY BATCH_ACCOUNT_KEY \
                     --BATCH_ACCOUNT_URL BATCH_ACCOUNT_URL \
                     --POOL_ID POOL_ID \
                     --NODE_OS_PUBLISHER NODE_OS_PUBLISHER \
                     --NODE_OS_OFFER NODE_OS_OFFER \
                     --NODE_OS_SKU NODE_OS_SKU \
                     --POOL_VM_SIZE POOL_VM_SIZE \
                     --POOL_NODE_COUNT POOL_NODE_COUNT \
                     --JOB_ID JOB_ID
                     [--debug]
```
