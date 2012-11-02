import hashlib

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

		hsub = hashlib.md5()
		hsub.update(substring)
		
		for i in range(len(string)-len(substring)+1):			
			hs = hashlib.md5()
			hs.update(string[i:i+len(substring)])
			if hs.digest() == hsub.digest():				
				if string[i:i+len(substring)] == substring:
					return i

			

		return -1

