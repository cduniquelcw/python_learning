numbers = list(range(1,11))
even_numbers = []
odd_numbers = []
print(numbers)
while numbers:
	for num in numbers:
		print(num)
		if num % 2 == 0:
			num = numbers.pop(0)#弹出后导致索引对应的元素改变，最终结果不对，想办法修改
			even_numbers.append(num)
			print(num)
			print('even')
		else:
			num = numbers.pop(0)
			odd_numbers.append(num)#奇数
			print(num)
			print('odd')

print(even_numbers)
print(odd_numbers)
print(numbers)