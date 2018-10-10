while True:
	try:
		x=int(input('input num1'))
		y=int(input('input num2'))
	except ValueError:
		msg='Pls enter 2 nums.'
		print(msg)
	else:
		print(x+y)

