class Employee():
	def __init__(self,last_name,first_name,salary):
		self.last_name=last_name.title()
		self.first_name=first_name.title()
		self.salary=int(salary)

	def give_rise(self,rise=5000):
		self.salary+=rise
