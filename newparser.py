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


for time, event in pairwise(split_log):
	ActivityEntry(time, event)

tempfile = open("tempLog2.tmp", 'w')
tempfile.close()







