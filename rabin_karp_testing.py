import unittest
from rabin_karp import rabin_karp

class RabinKarpTests(unittest.TestCase):
	""" Testing Rabin-Karp algorithm implementation  """
	def setUp(self):
		self.words = [("Lelo","LeloLelo", 0),
					  ("Lelo","leloLelo", 4),
					  ("a","stiojgps", -1),
					  ("o","stiojgps", 3),
					  ("g","stiojgps", 5),
					  ("Lelo","garbageLelogarbage", 7),
					  ("Ricardo", "qwerty _Ricardo_ qwerty", 8)
					 ]
	
	def testNull(self):
		self.assertEqual(rabin_karp(None, None), -1)

	def testEmpty(self):
		self.assertEqual(rabin_karp("",""), -1)
		self.assertEqual(rabin_karp(""," "), -1)		
		self.assertEqual(rabin_karp(" ",""), -1)		

	def testSubBigger(self):		
		self.assertEqual(rabin_karp("LeloLelo","lelo"), -1)

	def testWord(self):		
		for w in self.words:
			self.assertEqual(rabin_karp(w[0],w[1]), w[2])


if __name__ == '__main__':
    unittest.main()