##比较谁的总能量大
import numpy as np 

def Energy(file1,file2):
	data1 = np.loadtxt(file1)
	data2 = np.loadtxt(file2)

	print(data1.shape)
	print(data2.shape)

	data1_totenergy = np.sum(data1[:,3])
	print(data1_totenergy)
	data2_totenergy = np.sum(data2[:,3])
	print(data2_totenergy)

	return 

Energy('highlocalization_energy_tem78.dat','highlocalization_energy_tem209.dat')
# Energy('total_energy_tem78.dat','total_energy_tem209.dat')