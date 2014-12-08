import re

class ActivityEntry():

	#unformatted entry is the HTML line that comes direct from parser

	def __init__(self, time, desc):

		self.time = time
		temp = re.split('</*p>', desc)
		print temp[0]

		