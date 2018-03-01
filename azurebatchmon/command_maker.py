#! /usr/bin/env python

import sys, os, csv

def make_download(val,sec, recursive_flg):    

    cmd = 'docker run -v $PWD:/mnt '
    if recursive_flg:
        cmd += '-e INPUT_RECURSIVE={} '.format(val)
    else:
        cmd += '-e INPUT={} '.format(val)

    cmd += '-e STORAGE_ACCOUNT_KEY={} '.format(sec)
    cmd += '-e DIR=/mnt/input '
    cmd += 'ken01nn/lifecycle bash /lifecycle/download.sh '
    return cmd


