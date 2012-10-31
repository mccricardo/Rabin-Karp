class RabinKarp:
	def __init__(self):
		self.text = ""
		self.sub = ""

	def search(self, substring, string):
		if substring == None or string == None:
			return -1
		if substring == "" or string == "":
			return -1
			
		if len(substring) > len(string):
			return -1
