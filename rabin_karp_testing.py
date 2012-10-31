import unittest
from rabin_karp import RabinKarp


class RabinKarpTests(unittest.TestCase):
	""" Testing Rabin-Karp algorithm implementation  """
	def setUp(self):
		pass
	
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
		self.assertEqual(rk.search("Lelo","LeloLelo"), 0)
		

if __name__ == '__main__':
    unittest.main()