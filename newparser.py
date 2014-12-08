import re
import ActivityEntry.py

f = open("log.html", 'r')

for line in f:

	if re.match('\s*\<\s*table', line):
		event_list = line
		break



f.close()

time_re = re.compile('(\d\d:\d\d)')

for time, item in time_re.split(line):

	print '\n'

tempfile = open("tempLog2.tmp", 'w')
tempfile.close()