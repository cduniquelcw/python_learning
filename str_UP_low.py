#字符串大小写
name = "jaMes"
name_up=name.upper()
name_low=name.lower()
name_tit=name.title()
print("Hello "+name_tit+", would you like to learn some Python today?")
famous_name="Albert Einstein"
message="a person who never made a mistake never tried anything new."
print(famous_name+" once said:\n" +'"'+ message +'"')
test_name=" wang jiaying is a sb "#删除字符串空白
print('\t'+test_name)
print(test_name.lstrip())
print(test_name.rstrip())
print(test_name.strip())