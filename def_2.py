# 函数模块只需要函数，其他的需要被注释掉，调用的时候才不至于出错
def show_magicians(magicians):
	print("'Magicians' name:\n")
	for magician in magicians:
		print(magician)



def make_great(magicians):
	i = 0
	while i < len(magicians):
		magicians[i] =  'the Great ' + magicians[i]
		i += 1
	return magicians

def make_great2(list1):
	list2=[]
	for value in list1:
		value = 'the Great ' + str(value)
		list2.append(value)
	list1 = list2
	return list1

# a=[1,2,3]
# print(make_great2(a))
# make_great2(a)
# print(a)
# a=make_great2(a)#为何调用函数后未修改a的值呢？
# print(a)

# show_magicians(make_great(list_magicians[:]))#修改副本
# show_magicians(list_magicians)#原列表未变
# make_great(list_magicians)#修改列表
# show_magicians(list_magicians)#列表改变

def sandwich(*food):
	print("\nMake a sandwich with the fallowing toppings:")
	for topping in food:
		print('-' + topping)

# sandwich('egg')
# sandwich('breef','milk')

def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for k,v in user_info.items():
		profile[k]=v
	return profile
# my_profile=build_profile('z','x',location='cd',field='python')

# print(my_profile)

def make_car(brand,model,**car_info):
	car_dic={}
	car_dic['brand']=brand
	car_dic['model']=model
	for k,v in car_info.items():
		car_dic[k]=v
	return car_dic
# car=make_car('Honda','Outback',color='blue',Twopackge=True,used='Yes')
# print(car)