def display_message():
    """显示所学习知识"""
    print('Operation of function.')
display_message()

def favorite_book(title):
    print('One of my favorite book is ' + title.title() + '.')
favorite_book('base of python')

def make_shirt(size,string='I love python'):
    print('The shirt is ' + size + ', and it print ' + string + '.')
make_shirt('XXL','Wtf')
make_shirt('XL')

def discribe_city(city='ChengDu',country='China'):
    print(city + ' is in ' + country + '.')
discribe_city()
discribe_city('BeiJing')
discribe_city(country='China',city='GuangZhou')
discribe_city(country='ZhongGuo')
discribe_city('Parise','France')



def make_album(name,album):
    dir_album = {'name':name,'album':album}
    return dir_album
print(make_album('Jay','Yehuimei'))

def make_album(name,album,songs_num = ''):
    if songs_num:
        dir_album = {'name':name,'album':album,'songs_num':songs_num}
    else:
    	dir_album = {'name':name,'album':album}
    return dir_album

#在终端中运行时，此处需要空行，且空行中连Tab都不能有。原因未知。
while True:
	na = input('输入歌手姓名：')
	if na == 'q':
		break
	al = input('输入专辑名：')
	if al == 'q':
		break
	sn = input('输入歌曲数：')
	if sn == 'q':
		break
	out = make_album(na,al,sn)
	print(out)