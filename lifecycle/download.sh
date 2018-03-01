#!/bin/bash

# Let it fail when something failed
set -e

# This script is supposed to be used to download input files from
# Azure Storage.
# This script should be called for each 1 input (or input-recursive) file.
#

function precheck() {
  if [[ -z ${INPUT} && -z ${INPUT_RECURSIVE} ]]; then
    echo "Either of INPUT or INPUT_RECURSIVE must be specified to invoke 'download.sh'"
    exit 1
  fi
  if [[ -z ${STORAGE_ACCOUNT_KEY} ]]; then
    echo "STORAGE_ACCOUNT_KEY must be specified to invoke 'download.sh'"
    exit 1
  fi
  if [[ -z ${DIR} ]]; then
    echo "DIR must be specified to invoke 'download.sh'"
    exit 1
  fi
}

function download() {

  mkdir -p ${DIR}

  if [[ -n ${INPUT} ]]; then
     SRC=${INPUT}
  elif [[ -n ${INPUT_RECURSIVE} ]]; then
     SRC=${INPUT_RECURSIVE}
  fi
  SRC_FILE=`echo $SRC | sed -E 's/^.*(http|https):\/\/([^/]+)(.*)/\3/g'`
  DEST=${DIR}${SRC_FILE}

  if [[ -n ${INPUT_RECURSIVE} ]]; then
    CMD="azcopy --source $SRC --destination $DEST --source-key $STORAGE_ACCOUNT_KEY --recursive"
  else
    CMD="azcopy --source $SRC --destination $DEST --source-key $STORAGE_ACCOUNT_KEY"
  fi

  echo "Execution: ${CMD}"
  ${CMD} || exit $?
}

function __main__() {
  precheck
  download
}

__main__ $@

