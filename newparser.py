
import re

from ActivityEntry import ActivityEntry

from utils import pairwise



f = open("log.html", 'r')

for line in f:

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
	activity_log.append( ActivityEntry(time, event) )

for elem in activity_log:
        elem.print_vals()
        


tempfile = open("tempLog2.tmp", 'w')
tempfile.close()







