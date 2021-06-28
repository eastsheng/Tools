import numpy as np 
# 归一化
def EnergyMax(file):
	data = np.loadtxt(file)
	m,n=data.shape
	max_value = np.max(data[:,3])
	print("Max Value =",max_value)
	return max_value

def EnergyNormalize(file,savetxt,max_value):
	data = np.loadtxt(file)
	m,n=data.shape
	print('Total energy of data:',np.sum(data[:,3]))
	print('Average energy of data:',np.mean(data[:,3]))
	Nor_energy = (data[:,3]/max_value).reshape(m,1)
	Nor_data = np.hstack((data[:,:3],Nor_energy))
	np.savetxt(savetxt,Nor_data,fmt='%f',delimiter="  ")
	return 	



path = '../EnergyNormalization/'

file2 = path+'highlocalization_energy_tem209.dat'
file1 = path+'highlocalization_energy_tem78.dat'

save2 = path+'highlocalization_energy_tem_78.dat'
save1 = path+'highlocalization_energy_tem_209.dat'


# 对比k个能量文件中能量的大小，并根据最大值的做归一化
k = 2
max_list=[]
file_list = [file1,file2]
save_list = [save1,save2]

for i in range(k):
	data = file_list[i]
	max_v = EnergyMax(data)
	max_list.append(max_v)
max_value = max(max_list)

for i in range(k):
	data = file_list[i]
	save = save_list[i]
	EnergyNormalize(data,save,max_value)


