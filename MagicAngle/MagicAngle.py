import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from matplotlib.font_manager import FontProperties

def Angle(n,m):
	Number_data=open('NumberAtom.data','a')
	if m==0 and n==0:
		print("\n跳过m和n同时为0的情况,并设其角度为0\n")
		angle = 0.000
	else:
		x = (m**2+4*m*n+n**2)/(m**2+m*n+n**2)/2

		angle = np.arccos(x)*(180/np.pi)
		angle = round(angle,3)
	print('Angle=',angle,file=Number_data)
	return angle

#Angle(5,1)

def Number_of_Aotm(n,m):
	Number_data=open('NumberAtom.data','a')
	NOA = 32*(m**2+m*n+n**2)
	print('  (n,m) =','('+str(n)+','+str(m)+')',\
		'原子总数',NOA,'\n',file=Number_data)

	return print('\n扭转后异质结晶胞：\n',\
		'(n,m) =','('+str(n)+','+str(m)+')',\
		'原子总数',NOA,'\n')

#Number_of_Aotm(5,1)

def Heatmap(n_max,m_max,figure=True):
	angle_list=[]

	for i in range(n_max+1):
		for j in range(m_max+1):
			angle_list.append(Angle(i,j))
			Number_of_Aotm(i,j)

	angle_matrix = np.array(angle_list).reshape(n_max+1,m_max+1)
	
	plt.figure(figsize=(10,8))

	sns.set(font_scale=1.5)
	plt.rc('font',family='Times New Roman',size=18)
	sns.heatmap(angle_matrix,cmap='jet',linewidth=0.4).invert_yaxis()

	plt.title('Magic Angle Heatmap (n,m)')

	plt.xlabel('n',size=26,)
	plt.ylabel('m',size=26,)

	plt.savefig('angle_heatmap.tif',dpi=80)
	if figure==True:
		plt.show()
		plt.close()
	return

'''
Heatmap(n_max,m_max,figure=True)
'''
Heatmap(10,10,figure=True)
