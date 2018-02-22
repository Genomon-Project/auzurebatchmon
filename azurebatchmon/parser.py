#! /usr/bin/env python

from run import *
import argparse

def create_parser():

    parser = argparse.ArgumentParser(prog = "azurebatchmon")

    parser.add_argument("--version", action = "version", version = "azurebatchmon-0.1.0b1")

    parser.add_argument("script_file", metavar = "script.sh", default = None, type = str,
                        help = "")
    
    parser.add_argument("image", default = None, type = str,
                        help = "")
    
    parser.add_argument("task_file", metavar = "task.tsv", default = None, type = str,
                        help = "")

    parser.add_argument("--STORAGE_ACCOUNT_NAME", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--STORAGE_ACCOUNT_KEY", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--BATCH_ACCOUNT_NAME", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--BATCH_ACCOUNT_KEY", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--BATCH_ACCOUNT_URL", default = None, type = str, require = True,
                        help = "")


    parser.add_argument("--POOL_ID", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--NODE_OS_PUBLISHER", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--NODE_OS_OFFER", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--NODE_OS_SKU", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--POOL_VM_SIZE", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--POOL_NODE_COUNT", default = None, type = str, require = True,
                        help = "")

    parser.add_argument("--JOB_ID", default = None, type = str, require = True,
                        help = "")


    return parser
 

