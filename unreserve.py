#!/usr/bin/python
import os
import argparse
import subprocess

UNRESERVE = '/home/apvalmart/rtos_val/tools/support/bfunreserve'

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('board', nargs='+')
    args = p.parse_args()
    for b in args.board:
        name = os.path.basename(b)
        if name.endswith('.cfg'):
            name = name[:-len('.cfg')]
        subprocess.call([UNRESERVE, name])

