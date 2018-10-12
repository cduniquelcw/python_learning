import json

def get_stored_fn():
	file_name='favorite_number.json'
	try:
		with open(file_name)as f_obj:
			x=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return x

def store_new_fn():
	file_name='favorite_number.json'
	x=input('请输入你最喜欢的数字：')
	with open(file_name,'w')as f_obj:
		json.dump(x,f_obj)
		return x



def print_fn():
	x=get_stored_fn()
	while x:
		msg='Is your favorite number '+str(x)+'?\nY/N'
		ans=input(msg)
		if ans.lower() =='y':
			print('Thanks for coming back!')
			break
		elif ans.lower() =='n':
			x=store_new_fn()
			print('I will remember that your favorite number is '
					+x+' when you come back!')
			break
		else:
			continue
	if x ==None:
		x=store_new_fn()
		print('I will remember that your favorite number is '
				+x+' when you come back!')

print_fn()
