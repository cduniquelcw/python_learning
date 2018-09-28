dir_names={
	'first_name':'Zhu',
	'last_name':'X',
	'age':27,
	'city':'CD'
}
print(dir_names)
print('\n')

favorite_numbers={
	'zx':3,
	'wxj':7,
	'zj':23,
	'wap':6,
	'hlp':0,
}
for k,v in favorite_numbers.items():
	print(k.title()+"'s favorite number is "+str(v)+'.\n')

dir={
	'print':'print sth',
	'lower':'lower alphabet',
	'upper':'upper alphabet',
	'sorted':'in order',
	'title':'title alphabet'
}
print('Print: '+dir['print'].title()+'\n')

for k,v in dir.items():
	print(k.title()+': '+v.title()+'.')

	rivers_areas={'nile':'egypt','changjiang':'china','mississippi':'america',}
for k,v in rivers_areas.items():
	print('The '+k.title()+' runs through '+v.title()+'.')
	print(k.title())
	print(v.title()+'\n')

favorite_languages ={'jen':'python','sarah':'c','edward':'ruby','phil':'python',}
investigation_names=['jen','zj','ljj','sarah','ruby']
for i_name in investigation_names:
	if i_name.lower() in [f_name.lower() for f_name in favorite_languages]:
		print(i_name.title()+', thanks for participating.')
	else:
		print(i_name.title()+', please participate in.')
print('\n')

cities={
	'ChengDu':{
	'country':'China',
		'population':'16 millions',
		'fact':"lcw's favorite city.",
		},
	'Paris':{
		'country':'France',
		'population':'11 millions',
		'fact':'capital of France.',
		},
	'New York':{
		'country':'America',
		'population':'8.5 millions',
		'fact':'biggest city of America.',
		}
	}
for city,infos in cities.items():
	print('City: '+city.title())
	info1=infos['country']
	info2=infos['population']
	info3=infos['fact']
	print('Country: '+info1+'\tPopulation: '+info2+'\tFact: '+info3.title()+'\n')