class Restaurant():
	"""餐馆的名字，类型"""
	def __init__(self,restaurant_name,cuisine_type,):
		"""①直接修改属性的值"""
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		"""描述餐馆"""
		print(self.restaurant_name.title()
		 + ' is a ' + self.cuisine_type + ' restaurant.')
		print(str(self.number_served) + ' people have eaten here.')

	def open_restaurant(self):
		"""打印餐馆营业中。"""
		print(self.restaurant_name.title() + ' is opening.')

	def set_number_served(self,number):
		"""设置已服务人数。②通过方法修改属性的值"""
		self.number_served=number

	def increment_number_served(self,number):
		"""#③通过方法对属性的值进行递增"""
		self.number_served+=number





class User_info():
	"""docstring for User"""
	def __init__(self, first_name,last_name,*infos):
		self.first_name=first_name
		self.last_name=last_name
		self.infos=[]
		for info in infos:
			self.infos.append(info)
		self.login_attempts=0
	def describe_user(self):
		print(self.first_name+self.last_name)
		count =0
		while count < len(self.infos):
			print(self.infos[count])
			count +=1
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0
	def greet_user(self):
		print('Hello, ' + self.first_name + self.last_name + '.')


# class User_info2():
# 	"""docstring for User"""
# 	def __init__(self, first_name,last_name,**infos):
		
# 		self={}
# 		self[first_name]=first_name
# 		self[last_name]=last_name
# 		for k,v in infos.items():
# 			self[k]=v

# 	def describe_user(self):
# 		print(self[first_name]+self[last_name])
		
# 	def greet_user(self):
# 		print('Hello, ' + self[first_name] + self[last_name] + '.')

m_r=Restaurant('Jumantang','Hotpot')
print(m_r.restaurant_name.title())
print(m_r.cuisine_type.title())
m_r.describe_restaurant()
m_r.number_served=10
m_r.describe_restaurant()
m_r.set_number_served(5)
m_r.describe_restaurant()
m_r.increment_number_served(10)
m_r.describe_restaurant()
m_r.open_restaurant()

m_r2=Restaurant('2m2','Hotpot')
m_r3=Restaurant('mtf','home-cooking')
m_r2.describe_restaurant()
m_r3.describe_restaurant()

m_info=User_info('z','x','male','26')
m_info.describe_user()
m_info.greet_user()
m_info.increment_login_attempts()
print(m_info.login_attempts)

m_info.increment_login_attempts()
print(m_info.login_attempts)
m_info.reset_login_attempts()
print(m_info.login_attempts)


# m_info=User_info2('z','x','sexual':'male','age':'26')#，列表可以运行，字典不行
# m_info.describe_user()
# m_info.greet_user()
class IcecreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['vanilla','strawberry','chocolate','original']
	def print_flavors(self):
		for i in self.flavors:
			print(i)
		print(self.flavors)

my_ICS=IcecreamStand('Macdonald','dessert')
#my_ICS.flavors=['vanilla','strawberry','chocolate','original']
my_ICS.set_number_served(10)
my_ICS.describe_restaurant()
my_ICS.print_flavors()

class Privileges():
	def __init__(self,privileges=['can add post','can del post','can ban user']):
		self.privileges=privileges

	def show_priviledges(self):
		for privilege in self.privileges:
			print('Administrator '+privilege+'.')

class Administrator(User_info):
	def __init__(self,first_name,last_name,*infos):
		super().__init__(first_name,last_name,*infos)
		self.privileges=Privileges(['fuck'])



zx=Administrator('z','x','male',26)
zx.describe_user()
zx.privileges.show_priviledges()