prompt = 'What kind of ingredient do you want?'
prompt += "Enter 'quit' to end the program."
msg = ""
while msg != 'quit':#条件
	msg = input(prompt)
	if msg != 'quit':
		print("We'd add "+ str(msg) +' in the pizza!')

prompt = 'Tell me your age, tell you the cost.'
age = ""
active = True
while active:#标志
	age = int(input(prompt))
	if age < 3:
		cost = 0
	elif age < 12:
		cost = 10
	elif age > 12:
		cost = 15
	print('You will spend $' +str(cost) +' on this!')
	active = True
	if age == 0:
		break
		#active = False

#while True:# 无限循环
	#print('???')

