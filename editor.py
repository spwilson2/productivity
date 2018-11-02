#!/usr/bin/python3
'''
Script which wraps the gvim editor server to add functionality:

* Select which gvim server to use.
'''

# TODO Rather than use the DEFAULT_SERVER use a file to store the active server.
# TODO Add functionality to vim to set the current vim server.

import argparse
import os
import sys
import subprocess
import shlex

DEFAULT_SERVER = 'gvim'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='servername', default=DEFAULT_SERVER, type=str, action='store', help='server name')
    parser.add_argument('-n', dest='noblock',
            action='store_true',
            default=os.environ.get('noblock', False))
    parser.add_argument('--forward', default=[], dest='forwarded', nargs=argparse.REMAINDER)
    parser.add_argument('file', type=str, nargs='*')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    servername = args.servername
    files = args.file
    block = not args.noblock
    forwarded_args = args.forwarded

    if args.file:
        # Open all files in the server
        command = ['gvim']
        command.extend(forwarded_args)
        command.append('--servername')
        command.append(servername)
        command.append('--remote-tab')
        command.extend(files)
        # Eat the error message
        #
        # FIXME, just filter the expected error, not all of it
        # E247: no registered server named ""GVIM"": Send failed.
        #
        err_msg = subprocess.check_output(command, stderr=subprocess.STDOUT)
    else:
        # Try to open as a new tab.
        # If the server doesn't exist, open a whole process.
        try:
            command = ('gvim --servername {name}'
                    ' --remote-send :tabnew\n').format(name=servername)
            # Eat the error message
            #
            # FIXME, just filter the expected error, not all of it
            # E247: no registered server named ""GVIM"": Send failed.
            #
            err_msg = subprocess.check_output(
                    command.split(' '), 
                    stderr=subprocess.STDOUT)
        except:
            command = 'gvim --servername {name}'.format(name=servername)
            subprocess.check_call(command.split(' '))
    if block:
        input('Press enter when done editing: ')
