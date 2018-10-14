import unittest
from city_function import city_country
class Test_city_country(unittest.TestCase):
	"""测试city_function"""
	def test_city_country(self):
		"""是否能正确处理city+country"""
		out=city_country('santiago','chile')
		self.assertEqual(out,'Santiago, Chile')

	def test_city_country_population(self):
		""""""
		out=city_country('chengdu','china',12000000)
		self.assertEqual(out,'Chengdu, China - population=12000000')

unittest.main()