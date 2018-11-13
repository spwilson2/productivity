#!/usr/bin/python

'''
This script opens a log, makes sure there is a heading with the current date. 
If there is no header it appends it.
'''

import argparse
import datetime
import os
import re

now = datetime.datetime.now()
DATE = '%s-%s-%s' % (now.year, now.month, now.day)

parser = argparse.ArgumentParser()
parser.add_argument('log')
parser.add_argument('--date', default=DATE, required=False)

args = parser.parse_args()
log_filename = args.log


date_string = args.date
header_sym = '='
date_header = '%s\n%s' % (date_string, header_sym*len(date_string))

additional_headings = ['Complete', 'Notes', 'Todo']
heading_sym = '^'

if not os.path.isfile(log_filename):
    open(log_filename, 'w').close()

with open(log_filename, 'r+') as log:
    matches = re.findall(date_header, log.read())

    if not matches:
        log.write(date_header)
        log.write('\n')
        log.write('\n')

        for heading in additional_headings:
            log.write(heading)
            log.write('\n')
            log.write(heading_sym * len(heading))
            log.write('\n')
            log.write('\n')
