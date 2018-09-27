dir_names={
	'first_name':'Zhu',
	'last_name':'X',
	'age':27,
	'city':'CD'
}
print(dir_names)

favorite_numbers={
	'ZX':3,
	'Wxj':7,
	'zj':23,
	'wap':6,
	'hlp':0,
}
for k,v in favorite_numbers.items():
	print(k+"'s favorite number is "+str(v)+'.')
dir={
	'print':'print sth',
	'lower':'lower alphabet',
	'upper':'upper alphabet',
	'sorted':'in order',
	'title':'title alphabet'
}
print('Print: '+dir['print'].title())
for k,v in dir.items():
	print(k.title()+': '+v.title()+'.')