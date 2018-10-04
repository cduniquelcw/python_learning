class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name.title() + ' is a ' + self.cuisine_type + ' restaurant.')
	def open_restaurant(self):
		print(self.restaurant_name.title() + ' is opening.')

class User_info():
	"""docstring for User"""
	def __init__(self, first_name,last_name,*infos):
		self.first_name=first_name
		self.last_name=last_name
		self.infos=[]
		for info in infos:
			self.infos.append(info)
	def describe_user(self):
		print(self.first_name+self.last_name)
		count =0
		while count < len(self.infos):
			print(self.infos[count])
			count +=1
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
m_r.open_restaurant()

m_r2=Restaurant('2m2','Hotpot')
m_r3=Restaurant('mtf','home-cooking')
m_r2.describe_restaurant()
m_r3.describe_restaurant()

m_info=User_info('z','x','male','26')
m_info.describe_user()
m_info.greet_user()

# m_info=User_info2('z','x','sexual':'male','age':'26')#，列表可以运行，字典不行
# m_info.describe_user()
# m_info.greet_user()
