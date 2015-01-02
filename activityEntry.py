import re

class ActivityEntry():

	#unformatted entry is the HTML line that comes direct from parser

        def print_vals(self):
                print self.time
                print self.activity_num
                print self.activity
                print self.desc

	def __init__(self, time, desc):

		self.time = time
		temp = re.split('</*p>', desc)

                # default num
                activity_num = "n"
                possible_num = temp[0]
                
                # while loop to take chunks off end until activity_num is found
                while( 1 ):
                        try:
                                int(activity_num)
                                break
                        except ValueError:
                                activity_num = possible_num.rsplit(' ', 1)[-1]
                                possible_num = possible_num.rsplit(' ', 1)[0]
                                if( '' == possible_num ):
                                        break
                                        
                self.activity_num = activity_num
                self.activity = possible_num.strip()
        
                self.desc = temp[1]
                








