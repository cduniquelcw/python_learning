from def_2 import*
# 几种调用方式：
# import def_2  def_2.show_magicians
# import def_2 as d_2 d_2.show_magicians
# from def_2 import show_magicians
# from def_2 import show_magicians as sm
# from def_2 import*

list_magicians=['zx','zj','zz','zc','zm']
show_magicians(list_magicians)
name=make_great(list_magicians)
print(name)
print(list_magicians)
show_magicians(list_magicians)
