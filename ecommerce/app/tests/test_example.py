import unittest


class TestExample(unittest.TestCase):

	def test_example_1(self):
		self.assertEqual(10, 10)

	def test_example_2(self):
		self.assertNotEqual(10, 20)
