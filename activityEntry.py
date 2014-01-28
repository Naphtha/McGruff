class ActivityEntry():


	#unformatted entry is the HTML line that comes direct from parser

	def __init__(self, unformattedEntry):

		temp = unformattedEntry.split('<p>')
		print temp

		