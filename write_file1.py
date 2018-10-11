while True:
	with open('guest.txt','a')as f_obj:
		name=input('请输入您的姓名：')
		if name == 'q':
			break
		else:
			print('Hello '+name +'!')
			f_obj.write(name+'\n')
