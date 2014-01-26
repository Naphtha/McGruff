
from HTMLParser import HTMLParser

f = open("log.html", 'r')
tempfile = open("tempLog.tmp", 'w')
line = ""
flag = 0

for line in f:

	if "<h1>Daily Activity Log " in line:
		print line
		tempfile.write(line)
		
	if "*==========================================================================" in line:
		print line
		line = line.replace("*==========================================================================", "\n\n")
		tempfile.write(line)

f.close()
tempfile.close()

# tempfile = open("tempLog.tmp", 'r')

# for line in tempfile:

# 	for word in line:

# 		print word
# tempfile.close()