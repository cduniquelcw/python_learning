while True:
	try:
		x1=input('请输入第1个数字：')
		if x1=='q':
			break
		x=int(x1)
		y1=input('请输入第2个数字：')
		if y1=='q':
			break
		y=int(y1)
		print(str(x) +'+'+str(y)+'='+str(x+y))
	except ValueError:
		msg='请重新输入数字.'
		print(msg)