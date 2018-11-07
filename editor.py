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
import json

DEFAULT_SERVER = 'gvim'

def i3_get_active_pane():
    ''':returns: The name of the currently focused i3 panel/workspace.'''
    workspaces = subprocess.check_output('i3-msg -t get_workspaces'.split())
    workspaces = json.loads(workspaces)
    for workspace in workspaces:
        if workspace['focused']:
            return workspace['name']

def parse_args():

    # Try to use the currently active i3 panel as the default servername.
    i3_pane = i3_get_active_pane()
    if i3_pane is not None:
        default_server = i3_pane

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='servername', default=i3_pane, type=str, action='store', help='server name')
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

    if files:
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
        sp = subprocess.Popen(command, stderr=subprocess.STDOUT)
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
