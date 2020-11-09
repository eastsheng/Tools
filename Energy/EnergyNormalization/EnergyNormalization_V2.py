##比较谁的总能量大
import numpy as np 

def EnergyNormalize(file1,file2,savetxt1,savetxt2):
	data1 = np.loadtxt(file1)
	data2 = np.loadtxt(file2)
	m,n=data1.shape
	j,k=data2.shape
	# print(data1.shape)
	# print(data2.shape)

	max_value = np.max(data2[:,3])#按照第二个数据的最大值归一化
	# print(max_value)
	print('Total energy of data1:',np.sum(data1[:,3]))
	print('Total energy of data2:',np.sum(data2[:,3]))
	print('Average energy of data1:',np.mean(data1[:,3]))
	print('Average energy of data2:',np.mean(data2[:,3]))
	Nor_energy1 = (data1[:,3]/max_value).reshape(m,1)
	Nor_energy2 = (data2[:,3]/max_value).reshape(j,1)
	# print(Nor_energy1.shape)

	Nor_data1 = np.hstack((data1[:,:3],Nor_energy1))
	Nor_data2 = np.hstack((data2[:,:3],Nor_energy2))
	# print(Nor_data1)
	np.savetxt(savetxt1,Nor_data1,fmt='%f',delimiter="  ")
	np.savetxt(savetxt2,Nor_data2,fmt='%f',delimiter="  ")

	return print('Done!')


data2 = '25highlocalization.dat1'
data1 = '33highlocalization.dat1'

save2 = '25highlocalization.dat'
save1 = '33highlocalization.dat'

EnergyNormalize(data1,data2,save1,save2)
