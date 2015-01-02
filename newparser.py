# runs with python 2.7.5

import re
import sys
import json

# custom class
from activityEntry import ActivityEntry

# helper function
from utils import pairwise




f = open(sys.argv[1], 'r')

for line in f:
        
        # figure out the crime log date
        if "published" in line:
                log_date = line.split(">")[1].split("<")[0]
                

	if re.match('\s*\<\s*table', line):
		event_list = line
                break



f.close()

time_re = re.compile('(\d\d:\d\d)')

split_log = time_re.split(line)

if re.match( '\s*<table' ,split_log[0]):
	split_log.pop(0)

activity_log = []

for time, event in pairwise(split_log):
        temp_entry = ActivityEntry(time, event)
	activity_log.append( {"activity_num":temp_entry.activity_num, "time":temp_entry.time, "activity":temp_entry.activity, "desc":temp_entry.desc} )

        

file_name = sys.argv[1].rsplit(".html", 1)[0]





json_file = open( "".join( (file_name,".json") ), 'w')

# use to debug
# json.dump({log_date:[activity_log]}, json_file, indent=1)
json.dump({log_date:[activity_log]}, json_file, indent=1)

json_file.close()







