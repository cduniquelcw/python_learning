"""一个表示餐馆的模块"""

class Guest():
	"""定义客人的类"""
	def __init__(self,number_served=0):
		self.number_served=number_served

	def set_number_served(self,number):
		"""设置已服务人数。②通过方法修改属性的值"""
		self.number_served=number
	def increment_number_served(self,number=0):
		"""#③通过方法对属性的值进行递增"""
		if self.number_served+number < 50:
			self.number_served+=number#少于50人，最多还可以加9人
		else:
			self.number_served = 50#大于等于50人，则最多为50人
			print('Too many people.')


class Restaurant():
	"""餐馆的名字，类型"""
	def __init__(self,restaurant_name,cuisine_type,):
		"""①直接修改属性的值"""
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.guest=Guest()#初始化时有0个人served

	def describe_restaurant(self):
		"""描述餐馆"""
		print(self.restaurant_name
		 + ' is a ' + self.cuisine_type + ' restaurant.')
		print(str(self.guest.number_served) + ' people have eaten here.')

	def open_restaurant(self):
		"""打印餐馆营业中。"""
		print(self.restaurant_name.title() + ' is opening.')

class IcecreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['vanilla','strawberry','chocolate','original']
	def print_flavors(self):
		for i in self.flavors:
			print(i)#输出列表元素
		print(self.flavors)#输出列表

my_ICS=IcecreamStand('Macdonald','dessert')
#my_ICS.flavors=['vanilla','strawberry','chocolate','original']
my_ICS.guest.set_number_served(10)
my_ICS.describe_restaurant()
my_ICS.print_flavors()