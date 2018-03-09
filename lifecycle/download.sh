#!/bin/bash

# Let it fail when something failed
set -e

# This script is supposed to be used to download input files from
# Azure Storage.
# This script should be called for each 1 input (or input-recursive) file.
#

function precheck() {
  if [[ -z ${INPUT} && -z ${INPUT_RECURSIVE} && -z ${SCRIPT} ]]; then
    echo "Either of INPUT, INPUT_RECURSIVE or SCRIPT must be specified to invoke 'download.sh'"
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
  elif [[ -n ${SCRIPT} ]]; then
     SRC=${SCRIPT}
  fi
  SRC_FILE=`echo $SRC | sed -E 's/^.*(http|https):\/\/([^/]+)(.*)/\3/g'`
  DEST=${DIR}${SRC_FILE}

  if [[ -n ${INPUT_RECURSIVE} ]]; then
    CMD="azcopy --source $SRC --destination $DEST --source-key $STORAGE_ACCOUNT_KEY --recursive --quiet"
  else
    CMD="azcopy --source $SRC --destination $DEST --source-key $STORAGE_ACCOUNT_KEY --quiet"
  fi

  echo "Execution: ${CMD}"
  ${CMD} || exit $?
}

function __main__() {
  precheck
  download
}

__main__ $@

