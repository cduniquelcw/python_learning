import json

def get_stored_fn():
	"获取已存储的数字"
	file_name='favorite_number.json'
	try:
		with open(file_name)as f_obj:
			x=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return x

def get_new_fn():
	"获取新数字并存储"
	file_name='favorite_number.json'
	x=input('请输入你最喜欢的数字：')
	with open(file_name,'w')as f_obj:
		json.dump(x,f_obj)
		return x
def print_thanks():
	"打印谢谢。"
	print('Thanks for coming back!')

def print_remember(x):
	"打印已记住数字。"
	print('I will remember that your favorite number is '
				+x+' when you come back!')

def judge_yn(x):
	"判断是否是最喜欢的数字,并打印信息"
	while True:
		msg='Is your favorite number '+str(x)+'?\nY/N'
		ans=input(msg)
		if ans.lower() =='y':
			print_thanks
			break
		elif ans.lower() =='n':
			x=get_new_fn()
			print_remember(x)
			break
		else:
			continue


def print_fn():
	""
	x=get_stored_fn()
	if x:
		judge_yn(x)
	else:
		x=get_new_fn()
		print_remember(x)

print_fn()
