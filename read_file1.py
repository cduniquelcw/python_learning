with open('learning_python.txt')as file:
	whole_file=file
	print(whole_file)

	lines=file.readlines()
	all_lines=''
	for line in lines:
		all_lines+=line
		print(line.lstrip())
print(all_lines+'...')
