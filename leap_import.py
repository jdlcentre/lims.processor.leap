#!/usr/bin/python
import os.path

script_path = os.path.dirname(os.path.realpath(__file__))
zip_path = sys.argv[1]
igsn = sys.argv[2]
ar = sys.argv[3]

project_size = os.path.getsize(zip_path)


print 'Path to file, URL etc.' + ';' + str(project_size)
