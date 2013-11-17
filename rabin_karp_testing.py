import unittest
from rabin_karp import RabinKarp

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
		rk = RabinKarp()
		self.assertEqual(rk.search(None, None), -1)

	def testEmpty(self):
		rk = RabinKarp()
		self.assertEqual(rk.search("",""), -1)
		self.assertEqual(rk.search(""," "), -1)		
		self.assertEqual(rk.search(" ",""), -1)		

	def testSubBigger(self):
		rk = RabinKarp()
		self.assertEqual(rk.search("LeloLelo","lelo"), -1)

	def testWord(self):
		rk = RabinKarp()
		for w in self.words:
			self.assertEqual(rk.search(w[0],w[1]), w[2])


if __name__ == '__main__':
    unittest.main()