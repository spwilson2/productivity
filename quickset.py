#!/usr/bin/python

import argparse
import subprocess
import sys
import tempfile

import ghs

if __name__ == '__main__':
    p = argparse.ArgumentParser(
            description='Quickly run the rotator and setdtb scripts for a '
            'given board.')
    p.parse_known_args()
    args = ghs.get_forwarded_sys_args()

    d = tempfile.mkdtemp()
    f = subprocess.check_output([ghs.PATHS['rotator'], '--tempdir', d]  + args)
    f = f.rstrip()
    print('Generated device tree:')
    print(f)
    print('')
    subprocess.check_call([ghs.PATHS['setdtb']] + '--update -P'.split() + [f])
