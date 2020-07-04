import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def Angle(n,m):
	Number_data=open('result.data','a')
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
	Number_data=open('result.data','a')
	NOA = 32*(m**2+m*n+n**2)
	print('  (n,m) =','('+str(n)+','+str(m)+')',\
		'原子总数',NOA,'\n',file=Number_data)

	return NOA
	# print('\n扭转后异质结晶胞：\n',\
	# 	'(n,m) =','('+str(n)+','+str(m)+')',\
	# 	'原子总数',NOA,'\n')

#Number_of_Aotm(5,1)

def Heatmap(n_max,m_max,figure=True):
	angle_list=[]
	atomnumber_list=[]

	for i in range(n_max+1):
		for j in range(m_max+1):
			angle_list.append(Angle(i,j))
			atomnumber_list.append(Number_of_Aotm(i,j))

	angle_matrix = np.array(angle_list).reshape(n_max+1,m_max+1)
	atomnumber_matrix = np.array(atomnumber_list).reshape(n_max+1,m_max+1)
	# print(angle_matrix)
	# print(atomnumber_matrix)

	plt.figure(figsize=(24,8))
	plt.rc('font',family='Times New Roman',size=12)
	# sns.set()	

	plt.subplot(121)
	sns.heatmap(angle_matrix,vmin=0,vmax=60,square=True,cmap='jet',\
		linewidth=0.4,annot=True,fmt='.3').invert_yaxis()
	plt.title('Magic Angle Heatmap (n,m)',size=26)
	plt.xticks(size=22)
	plt.yticks(size=22)
	plt.xlabel('n',size=26,)
	plt.ylabel('m',size=26,)

	plt.subplot(122)
	sns.heatmap(atomnumber_matrix,vmin=0,vmax=10000,square=True,cmap='jet',\
		linewidth=0.4,annot=True,fmt='d').invert_yaxis()
	plt.title('Number of Atoms Heatmap (n,m)',size=26)
	plt.xticks(size=22)
	plt.yticks(size=22)	
	plt.xlabel('n',size=26,)
	plt.ylabel('m',size=26,)	

	plt.savefig('angle_heatmap.png',dpi=300)
	if figure==True:
		plt.show()
		plt.close()
	return

'''
Heatmap(n_max,m_max,figure=True)
'''
Heatmap(10,10,figure=True)
