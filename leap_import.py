#!/usr/bin/python
import os
from subprocess import call
import sys

script_path = os.path.dirname(os.path.realpath(__file__))
rhit_path = sys.argv[1]
igsn = sys.argv[2]
ar = str(sys.argv[3])

project_size = os.path.getsize(rhit_path)

with open('credentials.config', 'r') as f:
    credentials = f.readlines()

username = credentials[0]
password = credentials[1]
    
call(['python', 'ashell.py', 'login', username, password], stdout=open(os.devnull, 'wb'))

call(['python', 'ashell.py', 'cf Atom Probe Tomography + mkfolder ' + ar + ' + cf ' + ar + ' + mkfolder ' + igsn + ' + cf ' + igsn + ' + put ' + rhit_path], stdout=open(os.devnull, 'wb'))

call(['python', 'ashell.py', 'logout'], stdout=open(os.devnull, 'wb'))

print 'https://data.pawsey.org.au/public/?path=/Atom Probe Tomography/' + ar + '/' + igsn + '/' + os.path.basename(rhit_path) + ';' + str(project_size)
