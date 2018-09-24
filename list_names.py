name = ['zj','wd','ygz','bdt','wdm']#张捷、魏毒、洋鬼子、巴倒烫、伍短命
for i in name:#遍历
	print('Suprise '+i+', you motherfucker~')#Tab 是必须的
guests=['zj','wd','ygz']
for j in guests:
	print("I'd like to invite "+j+" to my dinner.")
print(guests[-1]+' is busy.')
guests[-1]='bdt'
print(guests)
guests.append('wdm')
print(guests)
guests.insert(2,'ljj')#刘佳佳
guests.insert(0,'wjy')#王佳营
print(guests)
pop_name=guests.pop(3)
print(pop_name+' is not invited.')
print(guests)
pop_name=guests.pop(3)
print(pop_name+' is not invited.')
print(guests)
del guests[0]
del guests[0]
del guests[0]
del guests[0]
print(guests)
length=len(guests)
print(length)