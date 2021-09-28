# plot density calculated by MD
import numpy as np
import matplotlib.pyplot as plt

def Density(densityfile,outstep=0,number_layer=80,inter_step=100,total_step=2177200):
	'''
	densityfile:密度文件
	outstep:要输出的哪一步时的密度分布
	number_layer:层数
	inter_step:密度输出间隔步数
	total_step:总步数
	'''
	sample = int(total_step/inter_step)
	sample_out = int(outstep/inter_step)
	timestep = 2e-3 #ps
	for i in range(sample):
		if i == sample_out:
			density_slice = np.loadtxt(densityfile,skiprows=4+(number_layer+1)*i,max_rows=number_layer)
			print(density_slice.shape,i*inter_step,"step",i*inter_step*timestep,"ps")

	x = density_slice[:,0]
	y = density_slice[:,3]
	# plt.rc('font', family='Times New Roman', size=16)
	# plt.figure(figsize=(10,6))
	# plt.plot(x,y,'r')
	# plt.xlabel('z(Å)',fontweight='bold',size=20)
	# plt.ylabel('Density(Number/$\mathregular{Å^3}$)',fontweight='bold',size=20)
	# plt.show()
	return x, y

# ---main program--- #
if __name__ == '__main__':

	outstep = 2000000
	number_layer = 80
	inter_step = 100
	total_step = 2177200
	x1,y1 = Density('1_all_density_Z_300K.dat',outstep=outstep,number_layer=number_layer,inter_step=inter_step,total_step=total_step)
	x2,y2 = Density('1_Sat_density_Z_300K.dat',outstep=outstep,number_layer=number_layer,inter_step=inter_step,total_step=total_step)
	x3,y3 = Density('1_Aro_density_Z_300K.dat',outstep=outstep,number_layer=number_layer,inter_step=inter_step,total_step=total_step)
	x4,y4 = Density('1_Res_density_Z_300K.dat',outstep=outstep,number_layer=number_layer,inter_step=inter_step,total_step=total_step)
	x5,y5 = Density('1_Asp_density_Z_300K.dat',outstep=outstep,number_layer=number_layer,inter_step=inter_step,total_step=total_step)
	plt.rc('font', family='Times New Roman', size=16)
	plt.figure(figsize=(10,6))
	plt.plot(x1,y1,'r',label='All')
	plt.plot(x2,y2,'b',label='Sat')
	plt.plot(x3,y3,'y',label='Aro')
	plt.plot(x4,y4,'g',label='Res')
	plt.plot(x5,y5,'gray',label='Asp')
	plt.legend()
	plt.xlabel('z(Å)',fontweight='bold',size=20)
	plt.ylabel('Density(Number/$\mathregular{Å^3}$)',fontweight='bold',size=20)
	plt.show()
