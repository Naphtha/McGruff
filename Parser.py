
from HTMLParser import HTMLParser
import re
import activityEntry

f = open("log.html", 'r')
tempfile = open("tempLog.tmp", 'w')
line = ""
flag = 0

for line in f:

	if "<h1>Daily Activity Log " in line:
		tempfile.write(line)
		
	if "*==========================================================================" in line:
		line = line.replace("*==========================================================================", "\n\n")
		tempfile.write(line)

f.close()
tempfile.close()



activities = []

tempfile = open("tempLog.tmp", 'r')

regex = re.compile('\d{2,2}:\d{2,2}')



for line in tempfile:

	matches = regex.search(line)

	if matches:

		tempActivity = activityEntry.ActivityEntry(line)
		activities.append(tempActivity)

		print matches.group()



tempfile.close()