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
    try:
        workspaces = subprocess.check_output('i3-msg -t get_workspaces'.split())
    except subprocess.CalledProcessError:
        return None
    workspaces = json.loads(workspaces)
    for workspace in workspaces:
        if workspace['focused']:
            return workspace['name']

def parse_args():
    # Try to use the currently active i3 panel as the default servername.
    i3_pane = i3_get_active_pane()
    if i3_pane is None:
        i3_pane = DEFAULT_SERVER

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='servername', default=i3_pane, type=str, action='store', help='server name')
    parser.add_argument('-n', dest='noblock',
            action='store_true',
            default=os.environ.get('noblock', False))
    #parser.add_argument('--forward', default=[], dest='forwarded', nargs=argparse.REMAINDER)
    parser.add_argument('file', type=str, nargs='*')
    args = parser.parse_args()
    return args

def vim_server_name_exists(server_name):
    servers = subprocess.check_output('gvim --serverlist'.split())
    # TODO Python2 backport
    servers = servers.decode('utf-8')
    val = server_name in servers.split('\n')
    return val

def vim_send(server_name, cmd):
    command = 'gvim --servername'.split()
    command.append(server_name)
    command.append('--remote-send')
    command.append(cmd)
    return subprocess.check_output(command, stderr=subprocess.STDOUT)

def vim_open_files(server_name, *paths):
    if not paths:
        if vim_server_name_exists(server_name):
            vim_send(server_name, ':tabnew\n')
        else:
            command = 'gvim --servername'.split()
            command.append(server_name)
            # TODO Assert output has the server doesn't exist message and nothing
            # else.
            subprocess.call(command, stderr=subprocess.STDOUT)
    else:
        command = 'gvim --servername'.split()
        command.append(server_name)
        command.append('--remote-tab')
        command.extend(paths)
        subprocess.check_call(command)

if __name__ == '__main__':
    args = parse_args()
    server_name = args.servername
    files = args.file
    block = not args.noblock

    #FIXME add support for the forwarded args in a separate subcommand
    #forwarded_args = args.forwarded

    vim_open_files(server_name, *files)
    if block:
        input('Press enter when done editing: ')
