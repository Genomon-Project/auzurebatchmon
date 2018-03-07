#!/bin/bash

# Let it fail when something failed
set -e

# This script is supposed to be used to upload output files to
# Azure Storage.
# This script should be called for just 1 time to upload "SRC" directory.
#

function precheck() {
  if [[ -z ${SRC} ]]; then
    echo "SOURCE variable is required but not provided"
    exit 1
  fi
  if [[ -z ${DEST} ]]; then
    echo "DEST variable is required but not provided"
    exit 1
  fi
  if [[ -z ${STORAGE_ACCOUNT_KEY} ]]; then
    echo "STORAGE_ACCOUNT_KEY must be specified to invoke 'upload.sh'"
    exit 1
  fi
}

function upload() {

  CMD="azcopy --source $SRC --destination $DEST --dest-key $STORAGE_ACCOUNT_KEY --recursive --quiet"

  echo "Execution: ${CMD}"
  ${CMD} || exit $?

}

function __main__() {
  precheck
  upload
}

__main__ $@

