import unittest
from Employee import Employee

class test_Employee(unittest.TestCase):
	def setUp(self):
		self.zs=Employee('san','zhang',35000)
		self.ls=Employee('si','li',42000)
		self.custom_rise=5201

	def test_give_default_rise(self):
		self.zs.give_rise()
		self.assertEqual(self.zs.salary,40000)

	def test_give_custom_rise(self):
		self.ls.give_rise(self.custom_rise)
		self.assertEqual(self.ls.salary,47201)

unittest.main()

