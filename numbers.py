numbers = list(range(1,11))
even_numbers = []
odd_numbers = []
print(numbers)
while numbers:
	num = numbers.pop(0)
	if num % 2 == 0:
		even_numbers.append(num)
	else:
		odd_numbers.append(num)#奇数
print(even_numbers)
print(odd_numbers)
print(numbers)