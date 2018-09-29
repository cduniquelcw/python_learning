prompt = 'What kind of ingredient do you want?'
prompt += "Enter 'quit' to end the program."
msg = ""
while msg != 'quit':#????
	msg = input(prompt)
	if msg != 'quit'
		print("We'd add "+ str(msg) +' in the pizza!')

prompt = 'Tell me your age, tell you the cost.'
age = ""
active = True
while active:#????
	age = input(prompt)
	if age < 3:
		cost = 0
	if age < 12:
		cost = 10
	if age > 12:
		cost = 15
	print('You will spend $' +str(cost) +' on this!')
	active = True
	if age = 'quit':
		break
		#active = False

while True:#????
	print('???')


sandwich_order=['pastrami','egg','pastrami','potato','breef','pastrami']
finished_sandwiches=[]
while sandwich_order:
	for sandwich in sandwich_order:
		if sandwich == 'pastrami':
			print(sandwich.title + ' was sold out!')
			sandwich_order.remove(sandwich)
		finished_sandwich=sandwich_order.pop()
		print('I made your '+ finished_sandwich +'sandwich.')
		finished_sandwiches.append(finished_sandwich)
	print(finished_sandwiches)

