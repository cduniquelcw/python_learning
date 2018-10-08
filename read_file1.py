with open('learning_python.txt')as file_objiect:
	whole_file=file_objiect.read()
	print(whole_file)#直接打印整个文件

#with open('learning_python.txt')as file_objiect:------#重新读取文件
	all_lines=''
	for line in open('learning_python.txt'):
	#for line in file_objiect:------#需要在前面重新读取文件，不然就没有输出
		all_lines+=line
		line_change=line.replace('Python','C++')
		print(line.strip())#遍历每一行并打印
		print(line_change.strip())

print(all_lines+'...')#各行储存起来，with外打印