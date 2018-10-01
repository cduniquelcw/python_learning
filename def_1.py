def display_message():
	"""显示所学习知识"""
	print('Operation of function.')
display_message()

def favorite_book(title):
	print('One of my favorite book is ' + title.title() + '.')
favorite_book('base of python')

def make_shirt(size,string='I love python'):
	print('The shirt is ' + size + ', and it print ' + string + '.')
make_shirt('XXL','Wtf')
make_shirt('XL')

def discribe_city(city='ChengDu',country='China'):
	print(city + ' is in ' + country + '.')
discribe_city()
discribe_city('BeiJing')
discribe_city(country='China',city='GuangZhou')
discribe_city(country='ZhongGuo')
discribe_city('Parise','France')

