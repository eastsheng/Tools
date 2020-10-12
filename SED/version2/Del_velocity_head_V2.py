import numpy as np
np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)  #输出所有的数组，不省略

def Del_Head(velocity_data,dvelocity_data):
	velocity = np.loadtxt(velocity_data,skiprows=9)
	# print(velocity)
	np.savetxt(dvelocity_data,velocity,fmt='%d %.6f %.6f %.6f')
	return 


# Del_Head('velocity.10010.CB.txt','wvelocity.10010.CB.txt')

# Main Program
print('---Start---')

i = 10010
# while i<=60000:
while i<=10010:
	Del_Head('velocity.'+str(i)+'.CB.txt','wvelocity.'+str(i)+'.CB.txt')
	print(str(i))
	i = i + 10
print('---Done!---')