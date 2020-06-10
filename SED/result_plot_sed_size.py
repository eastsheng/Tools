import numpy as np
import pandas as pd
import math as ma
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib.font_manager import FontProperties
from matplotlib import axes
from scipy.interpolate import interp2d

#----------variable---------------------#
ft = 99.96#frequency max                #
fi = 0.04#frequency interval            #
nf = int(ft/fi+1)#numbers of frequency  #
nuc = 80#numbers of unit cells          #
vector_resolution =   2.500000e-02#   #8.333333e-02#  4.000000e-02# 
T = 300#K
Freq = 50#THz                                #
#----------variable---------------------#

np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

frequency = [i for i in np.arange(0,ft+fi/10,fi)]
# print(frequency)
F = np.array(frequency).reshape(nf,1)
print(F)
#####------------------modify-sed-data
with open('result.sed_graphene'+str(nuc))as sed1:#, open('sed.dat','w')as sed2:

	line = sed1.readline()
	sed_list1 = []
	while line:
		num = list(map(float,line.split()))
		sed_list1.append(num)
		line = sed1.readline()
	sed1.close()
	sed_array1 = np.array(sed_list1).reshape(((int(nuc/2)+1)*nf,3))
	# print(sed_array1.shape)
	# print(sed_array1)
	# print(sed_array1[:,2])
	sed_array2 = sed_array1[:,2].reshape((nf,int(nuc/2)+1))
	sed_array3 = np.append(F,sed_array2,axis=1)
	print(sed_array3.shape)
	np.savetxt('sed_result.dat_graphene'+str(nuc),sed_array3,delimiter = ' ')
#####----------------modify-sed-data-save

#sed范围

#功能：找到矩阵最大值
def find_martrix_max_value(data_matrix):
    new_data=[]
    for i in range(len(data_matrix)):
        new_data.append(max(data_matrix[i]))
    print('SED data_matrix 最大值为：', max(new_data),np.log10(max(new_data)/100))#ma.log(max(new_data)/100,10))
find_martrix_max_value(sed_array2)
#功能：找到矩阵最小值
def find_martrix_min_value(data_matrix):
    new_data=[]
    for i in range(len(data_matrix)):
        new_data.append(min(data_matrix[i]))
    print('SED data_matrix 最小值为：', min(new_data),np.log10(min(new_data)/100))#ma.log(min(new_data)/100,10))
find_martrix_min_value(sed_array2)


###plot-sed
x = [i for i in np.arange(0,1.00001,vector_resolution)] #vector-can be found from result.sed
y = sed_array3[0:int(nf/2)+1 ,0]#frequency-只画0-50THz  int(nf/2)+1 int(nf*0.555)+1
x,y = np.meshgrid(x,y)
# print(y)
z = sed_array2[0:int(nf/2)+1,:]#sed
z = np.log10(z/100)#log of sed
z = z/np.max(z)#normalied
# xlabel = [0,0.2,0.4,0.6,0.8,1.0]
# ylabel = [0,10,20,30,40,50]
#font and size
font = FontProperties(fname='C:\\Windows\\Fonts\\times.ttf')

plt.figure(figsize=(6,10))
#plot
plt.pcolormesh(x,y,z,cmap='jet',shading='gouraud')#rainbow  gouraud  
#norm=colors.LogNorm(vmin = z.min(),vmax = z.max()),


#--------colorbar
cb=plt.colorbar(shrink=0.8)#,fraction=.1)
cb.set_label('Normalied log of spectral energy density',fontproperties=font,size=16)
# cb.set_ticks(np.linspace(0,8.3,4))
# cb.set_ticklabels( ('2','4','6','8'))
cb.ax.tick_params(labelsize=16)#,labelright=False)
for l in cb.ax.yaxis.get_ticklabels():
	l.set_family('Times New Roman')
#----------

#title and x y label
#####----------------modify-sed-title
plt.title('Length-y ('+str(nuc*0.4864)+' nm)',fontproperties=font,size=22)

plt.xlabel('Normalied wave vector',fontproperties=font,size=22)
plt.xticks(fontproperties=font,size=22)
plt.ylabel('Frequency (THz)',fontproperties=font,size=22)
plt.yticks(fontproperties=font,size=22)
# plt.tick_params(labelsize=16)
# plt.xlim(0,1)
# plt.ylim(0,20)
#save
#####----------------modify-sed-name-fig-save
plt.savefig('graphene'+str(nuc)+'_'+str(Freq)+'THz.png',dpi=300.0)
plt.show()
plt.close()


