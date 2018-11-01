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

DEFAULT_SERVER = 'gvim'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='servername', default=DEFAULT_SERVER, type=str, action='store', help='server name')
    parser.add_argument('-n', dest='noblock',
            action='store_true',
            default=os.environ.get('noblock', False))
    parser.add_argument('file', nargs='*')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    servername = args.servername
    files = args.file
    block = not args.noblock

    if args.file:
        # Open all files in the server

        files = ' '.join(files)
        command = ('gvim --servername "{name}"'
                ' --remote-tab'
                ' {files}').format(files=files, name=servername)
        subprocess.check_call(command, shell='/bin/bash')
    else:
        # Try to open

        try:
            command = ('gvim --servername "{name}"'
                    ' --remote-send \t\t:tabnew\n').format(name=servername)

            # Eat the error message
            #
            # FIXME, just filter the expected error, not all of it
            # E247: no registered server named ""GVIM"": Send failed.
            #
            err_msg = subprocess.check_output(
                    command.split(' '), 
                    stderr=subprocess.STDOUT)
        except:
            command = 'gvim --servername "{name}"'.format(name=servername)
            subprocess.check_call(command.split(' '))
    if block:
        input('Press enter when done editing: ')
