from collections import OrderedDict

py_dict=OrderedDict()
py_dict['print']='print sth'
py_dict['lower']='lower alphabet'
py_dict['upper']='upper alphabet'
py_dict['sorted']='in order'
py_dict['title']='title alphabet'

for k,v in py_dict.items():
	print(k.title()+': '+v.title()+'.')

from random import randint

class Die():
	"""骰子的类"""
	def __init__(self, sides=6):
		self.sides = sides
	def roll_die(self):
		self.x=randint(1,self.sides)
		print(self.x)

my_die=Die(6)
for i in range(1,11):
	my_die.roll_die()
print('\n')
my_die.sides=10
my_die2=Die(20)
for i in range(1,11):
	my_die.roll_die()#10面骰子扔10次
	my_die2.roll_die()#20面骰子扔10次




		