class User_info():
	"""用户名信息的类"""
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
		print('Login attempts number is '+str(self.login_attempts)+'.')

	def reset_login_attempts(self):
		self.login_attempts=0

	def greet_user(self):
		print('Hello, ' + self.first_name + self.last_name + '.')


# class User_info2():
# 	"""docstring for User"""
# 	def __init__(self, first_name,last_name,**infos):#，列表可以运行，字典不行
		
# 		self={}
# 		self[first_name]=first_name
# 		self[last_name]=last_name
# 		for k,v in infos.items():
# 			self[k]=v

# 	def describe_user(self):
# 		print(self[first_name]+self[last_name])
		
# 	def greet_user(self):
# 		print('Hello, ' + self[first_name] + self[last_name] + '.')



class Privileges():
	"""用户权限的类"""
	def __init__(self,privileges=['can add post','can del post','can ban user']):
		self.privileges=privileges

	def show_priviledges(self):
		for privilege in self.privileges:
			print('Admin '+privilege+'.')

class Admin(User_info):
	"""管理员的类"""
	def __init__(self,first_name,last_name,*infos):
		super().__init__(first_name,last_name,*infos)
		self.privileges=Privileges(['fuck'])#fuck字符串
		#self.privileges=Privileges('fuck')#f u c k 分行输出



