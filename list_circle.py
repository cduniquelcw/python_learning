animals=['dog','cat','rabbit','tiger','snake','dragon','horse']
for animal in animals:
	print('A '+animal+' would make a great pet.')
print("Any of those animal would make a great pet.")
print('The first 3 items in the lists are : '+str(animals[0:3]))
numbers=list(range(1,21))
print(numbers)
numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
odd_numbers=list(range(1,20,2))
print(odd_numbers)#打印列表
for odd_number in odd_numbers:
	print(odd_number)#打印元素
three_times_numbers=list(range(3,31,3))
for three_times_number in three_times_numbers:
	print(three_times_number)
cubes=[number**3 for number in range (1,11)]#立方解析
print(cubes)