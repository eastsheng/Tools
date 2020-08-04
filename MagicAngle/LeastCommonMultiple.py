#计算转角后两层结构晶格常数的最小公倍数

'''
找出最大值
'''
def Max(x,y):
	if x>y:
		M = x
	else:
		M = y
	return M
'''
找出最小公倍数
'''

def LeastCM(a1,a2,er):
	maxA = Max(a1,a2)

	global lcmA

	while(True):
		if ((maxA % a1 < er) and (maxA % a2 < er)):
			lcmA = maxA
			break

		maxA += 1
	print('\nLeast Common Multiple:',lcmA,'A')
	print('Multiple_1=',int(round(lcmA/a1,0)))
	print('Multiple_2=',int(round(lcmA/a2,0)))

	return lcmA

#replicate size
def Build(length):
	Times_number = int(round((length*10)/lcmA,0))

	print('Number of Times',Times_number)
	print('error = ',round(length-Times_number*lcmA/10,5))
	return 

##--Main--##
'''
a1是扭转后的a,a2是固定层石墨烯的a
leastCM找到最小公倍数
Build给个尺寸(nm)，输出需要replicate的大概倍数
'''
er=2.0 #误差，单位埃A，误差越小原胞越大。

#armchair
a1,a2 = [8.424,4.212]
LeastCM(a1,a2,er)
Build(50)#nm

#zigzag
b1,b2 = [4.864,2.432]
LeastCM(b1,b2,er)
Build(5)#nm



