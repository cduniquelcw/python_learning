alien_color='green'
if alien_color == 'green':
	print("You've gotten 5 points!")
elif alien_color =='yellow':
	print("You've gotten 10 points!")
elif alien_color == 'red':
	print("You've gotten 15 points!")

favorite_fruits=['apple','banana','peach',]
if 'apple' in favorite_fruits:
	print('You really like apple!')
if 'pear' not in favorite_fruits:
	print("You don't like pear!")
if 'banana' in favorite_fruits:
	print('You really like banana!')
if 'peach' in favorite_fruits:
	print('You really like peach!')

users_name=['Zx','Zj','wxj','ljj','admin']
#users_name=[]
if users_name:
	for user_name in sorted(users_name):
		if user_name == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print('Hello '+user_name+', thank you for logging again.')
else:
	print('We need to find some users.')

current_users=users_name
new_users=['ZX','zj','Wap','ty','hlp',]
for new_user in new_users:
	if new_user.lower() in [current_user.lower() for current_user in current_users]:#列表中忽略大小写的比较方法
		print(new_user+': You need input other name.')
	else:
		print(new_user+': This name was not used.')

number_list=list(range(1,10))
for number in number_list:
	if number == 1:
		print(str(number)+'st')
	elif number == 2:
		print(str(number)+'nd')
	elif number == 3:
		print(str(number)+'rd')
	else:
		print(str(number)+'th')