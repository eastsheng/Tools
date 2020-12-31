#write data for transmission
import matplotlib.pyplot as plt
import numpy as np
##############################################
#系统尺寸(nm)
# system_size_x = 21.640764864316765
# system_size_y = 5.000758001091962
system_size_z = 0.61
#系统温度(K)
System_temp = 300

#分层
number_layers = 200

number_fixed = 2
number_bath = 2

layers_fixed = [1,2,number_layers-1,number_layers]

#单位换算
timestep=5e-7#ns
J2ev=1.602763e-19#ev转换为J
tot_steps=2e7

#热流拟合区间(ns)
Energy_xmin=0.2#ns
Energy_xmax=timestep*tot_steps-0.2#ns
# #温度拟合区间(nm)
# Temp_xmin=1#nm
# Temp_xmax=system_size_x-1#nm
##############################################
#从NPTdata中读取并计算系统长宽，以便计算TC
def size(NPT_data):
	global system_size_x
	global system_size_y
	with open(NPT_data,'r')as data:
		for line in data:
			# print(line)
			line = line.strip().split()
			length_line = len(line)
			# print(length_line)
			if length_line==4 and line[2] in ['xlo','ylo','zlo']:
				print(line)
				if line[2]=='xlo':
					system_size_x = (float(line[1])-float(line[0]))/10#nm
					print('xhi-xlo=',system_size_x,'nm')
				elif line[2]=='ylo':
					system_size_y = (float(line[1])-float(line[0]))/10#nm
					print('yhi-xlo=',system_size_y,'nm')
				# elif line[2]=='zlo':
				# 	system_size_z = (float(line[1])-float(line[0]))/10#nm
				# 	print(system_size_z)
				# return	
				print('\n')				

# size('MoS2.data')
					

#------------------定义一个函数计算温度梯度--------------------#
def temp_grad(filename1,filename2):
	#filename1:原文件名，filename2：处理后要保存的文件名
	with open(filename1) as temp_11,\
		open(filename2,"w") as temp_12:
		for index, line in enumerate(temp_11,1):
			temp_gradient = line.strip().split()
			len_temp = len(temp_gradient)
			# print(len_temp)
			if len_temp == 4 and temp_gradient[0] is not '#' :
				coord = float(temp_gradient[0]) #x(nm)
				coord1=round(coord*(system_size_x/number_layers),4)
				temperature = round(float(temp_gradient[3]),4)#T(K)
				# print(coord,temperature)
				temp_12.write(str(coord))
				temp_12.write(" ")
				temp_12.write(str(coord1))
				temp_12.write(" ")
				temp_12.write(str(temperature))
				temp_12.write("\n")
	return 

#----------------------定义一个画温度分布的函数------------------------#
def plot_temp(filename2):
	#绘制温度分布并拟合。
	temp_12=open(filename2,"r")
	# print(temp_12.read())
	# xmin=5#nm
	# xmax=50#nm
	x1=list()
	y1=list()#全部
	x2=list()
	y2=list()#拟合
	for lines in temp_12:
		temp_gradient1 = lines.strip().split()
		temp_gradient  = list(map(eval,temp_gradient1))
		# print(temp_gradient)
		if temp_gradient[0] not in layers_fixed:

			x1.append(temp_gradient[1])
			y1.append(temp_gradient[2])

			if float(temp_gradient[1])>=Temp_xmin and float(temp_gradient[1])<=Temp_xmax:
				x2.append(temp_gradient[1])
				y2.append(temp_gradient[2])
				# print(type(temp_gradient[1]))
	fit = np.polyfit(x2,y2,1)#用1次多项式拟合
	fit_fn = np.poly1d(fit)
	print("拟合公式:",fit_fn)#拟合多项式
	print("斜率-温度梯度:" ,fit[0],"(K/nm)","\n"+"截距:",fit[1],"(K)","\n")
	global Temperature_gradient
	Temperature_gradient=fit[0]
	#-------坐标图
	plt.scatter(x1,y1)
	plt.plot(x2,fit_fn(x2),"r-",linewidth=4.0)
	plt.title("Temperature profile")
	plt.xlabel("Distance (nm)")
	plt.ylabel("Temperature (K)")
	plt.savefig("Temperature profile.png")
	plt.show()
	plt.close()
	return
# temp_grad("2_temp_equ_300K.dat","2_temp_equ_300K.txt")
# plot_temp("2_temp_equ_300K.txt")
#计算DeltaT for Transmission
def DeltaT_calculate():
	DeltaT = -Temperature_gradient*system_size_x
	print('Temperature_gradient=',Temperature_gradient,'K/nm')
	print('system_size_x=',system_size_x,'nm')
	print('DeltaT=',round(DeltaT,4),'K')
	return


##*********main program*********##
size('1_nvt.data')
# #温度拟合区间(nm)
# size_layer = system_size_x/number_layers
# Temp_xmin=(number_layers/6)*size_layer#nm
# Temp_xmax=system_size_x-Temp_xmin#nm

size_layer = system_size_x/number_layers
Temp_xmin=(number_fixed+number_bath)*size_layer#nm
Temp_xmax=system_size_x-Temp_xmin#nm

temp_grad("1_temp_equ_300K.dat","1_temp_equ_300K.txt")
plot_temp("1_temp_equ_300K.txt")
DeltaT_calculate()



print('*******************')
print('****   Done!   ****')
print('****   Done!   ****')
print('*******************')