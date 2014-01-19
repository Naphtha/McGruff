


f = open("log.html", 'r')
tempfile = open("tempLog.tmp", 'w')
line = ""

for line in f:

	if "Daily Activity Log" in line:
		print line

	if "</article></div>" in line:
		print line


f.close()
tempfile.close()

