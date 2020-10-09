import numpy as np
# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)  #输出所有的数组，不省略

def Del_Head(velocity_data,dvelocity_data):
	velocity = np.loadtxt(velocity_data,skiprows=9)
	# print(velocity)
	np.savetxt(dvelocity_data,velocity)
	return print("Done!")	


# Del_Head('velocity.10010.CB.txt','wvelocity.10010.CB.txt')

i = 10010
while i<=60000:
	Del_Head('velocity.'+str(i)+'.S8.txt','wvelocity.'+str(i)+'.S8.txt')
	print(str(i))
	i = i + 10