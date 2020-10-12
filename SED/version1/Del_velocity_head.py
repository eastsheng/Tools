import numpy as np
np.set_printoptions(suppress=True)
#np.set_printoptions(threshold=100000000)  #输出所有的数组，不省略

b = [i for i in range(1,8001)]
b = list(map(str,b))
# print(type(b[1]))
# print(b)
#去掉周期性表头
def peroid_sort(filename1,filename2):
	print("wait.....peroid sorting")
	with open(filename1) as reader, open(filename2, 'w') as writer:
		# print(reader.read())
		for index,line in enumerate(reader,1):
			# print(line)
			vels = line.strip().split()
			# print(len(vels))
			len_v=len(vels)
			number_id = vels[0]
			# print(type(number_id))
			if number_id in b and len_v == 4:
				# print('1111')
				writer.write(str(vels[0]))
				writer.write(' ')			
				writer.write(str(vels[1]))
				writer.write(' ')
				writer.write(str(vels[2]))
				writer.write(' ')
				writer.write(str(vels[3]))
				writer.write('\n')
	return "peroid sort done!"	

#peroid_sort('velocity.10000.C3B.txt','velocity.10000.-C3B.txt')
i = 10010
while i<=60000:
	peroid_sort('velocity.'+str(i)+'.S8.txt','wvelocity.'+str(i)+'.S8.txt')
	print(str(i))
	i = i + 10