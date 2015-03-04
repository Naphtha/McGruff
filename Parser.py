# runs with python 2.7.5
# run with python Parser.py <filename>

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
                

	# NOTE: never use RE in html parsing
	# the webpage's format is awful so instead of writing something that will
	# stand the test of time, I did this
	# also as i've noticed the format they upload the logs in is inconsistent so I just hacked this together
	if re.match('.*\<\s*table', line):
		event_list = line
		break

f.close()

# split activity log up by substrings that look like times e.g. 12:35
time_re = re.compile('(\d\d:\d\d)')
split_log = time_re.split(line)

# until first item in list is a time discard
while( None == time_re.match(split_log[0]) ):
	split_log.pop(0)


activity_log = []

# take pairs of items from list and parse
for time, event in pairwise(split_log):
	temp_entry = ActivityEntry(time, event, log_date)
	# append attributes to list
	activity_log.append( {"activity_num":temp_entry.activity_num, "time":temp_entry.time, "activity":temp_entry.activity, "desc":temp_entry.desc} )


file_name = sys.argv[1].rsplit(".html", 1)[0]

# check if the log already exists in the json
exists_flag = 0
try:
	with open( "orig.json", 'r' ) as json_file:

		for line in json_file:
			json_data = json.loads(line)
			try:
				json_data[log_date]
				exists_flag = 1
			except KeyError:
				pass
except ValueError:
	pass

# if we didn't find the item in the json file add it
if( 0 == exists_flag ):
	with open("orig.json", "a") as json_file:
		json_file.write( "{}\n".format( json.dumps({log_date:activity_log}) ) )

# open input file
with open("orig.json", "r+" ) as json_file:
	# open output file and rewrite contents
	with open("log.json", "w") as temp_file:
		first = json_file.readline()
		temp_file.write( first[0:-2] + '\n' )
		for line in json_file:
			temp_file.write( ',' + line[1:-2] + '\n' )
		temp_file.write('}\n')







