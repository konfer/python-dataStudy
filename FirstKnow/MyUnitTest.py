import unittest


class MyDict(object):
	pass


class TestMydDict(unittest.TestCase):
	def test_init(self):
		print("测试前准备")
	
	def tearDown(self):
		print("测试后准备")
	
	def test_init(self):
		md = MyDict(one = 1, two = 2)
		self.assertEqual(md['one'],1)
		self.assertEqual(md['two'],2)
		
	def test_nothing(self):
		pass
	
if __name__=='_main_':
	unittest.main()