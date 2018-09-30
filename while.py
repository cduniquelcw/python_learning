sandwich_order=['pastrami','egg','pastrami','potato','breef','pastrami','pastrami']
finished_sandwiches=[]
print('Pastrami was sold out.')

while 'pastrami' in sandwich_order:
	sandwich_order.remove('pastrami')
for sandwich in sandwich_order:
	print('I made your '+ sandwich +' sandwich.')#对于for循环，其中遍历是按照索引从1到-1来的，因此在遍历的过程中删除列表中的元素会导致1到-1对应元素的改变，不可避免出错
	finished_sandwiches.append(sandwich)
print(finished_sandwiches)
