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
		temp = log_date.split(" ")
		if( 1 == len(temp[1]) ):
			temp[1] = "0" + temp[1]
		log_date = temp[0] + temp[1] + temp[2]
                

	if re.match('.*\<\s*table', line):
		event_list = line
		break

f.close()

# split activity log up by substrings that look like times e.g. 12:35
time_re = re.compile('(\d\d:\d\d)')
split_log = time_re.split(line)

# until first item in list is a time discard
while( None == time_re.match(split_log[0]) ):
	print split_log[0]
	split_log.pop(0)


activity_log = []

# take pairs of items from list and parse
for time, event in pairwise(split_log):
	temp_entry = ActivityEntry(time, event)
	# append attributes to list
	activity_log.append( {"activity_num":temp_entry.activity_num, "time":temp_entry.time, "activity":temp_entry.activity, "desc":temp_entry.desc} )


file_name = sys.argv[1].rsplit(".html", 1)[0]





json_file = open( "".join( (file_name,".json") ), 'w')

json.dump({log_date:[activity_log]}, json_file, indent=1)

json_file.close()







