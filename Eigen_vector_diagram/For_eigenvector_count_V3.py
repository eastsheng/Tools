# Eigenvector Amplitude vs Count 

import numpy as np 
import matplotlib.pyplot as plt 
from brokenaxes import brokenaxes

# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)
class CountEigenVector(object):
	"""docstring for Count"""
	def __init__(self,data):
		super(CountEigenVector, self).__init__()
		self.data = data
		
	def count(self,bar_number,e):
		ovito = np.loadtxt(self.data,skiprows=2,usecols=(4,5,6),dtype=str)
		mix_eigenvector = ovito.reshape((-1,1)).astype(np.float)
		mix_eigenvector = np.abs(mix_eigenvector)
		# print(mix_eigenvector)

		l_xev = len(mix_eigenvector)

		max_vector = np.max(mix_eigenvector)
		min_vector = np.min(mix_eigenvector)

		scale = (max_vector-min_vector)/bar_number
		count = []
		for j in range(bar_number):
			count.append([])

		for i in range(l_xev):
			for j in range(bar_number):

				if mix_eigenvector[i]>=e:
					if mix_eigenvector[i]>=min_vector+scale*(j) and mix_eigenvector[i]<min_vector+scale*(j+1):
						count[j].append(mix_eigenvector[i].tolist())
						# print(mix_eigenvector[i])				
					else:
						pass


		Eigenvector_Amplitude = np.linspace(min_vector,max_vector,num=bar_number)
		
		len_count = []
		for j in range(bar_number):
			len_count.append(len(count[j]))

		print(Eigenvector_Amplitude,len_count)

		return Eigenvector_Amplitude,len_count

	def part1count(self,part,bar_number):
		# 因为顺序一致，所以这里直接按照顺序来代替序号
		ovito = np.loadtxt(self.data,skiprows=2,usecols=(4,5,6),dtype=str)
		# print(ovito[:,0])
		mix_eigenvector = []
		for i in range(len(part)):
			
			apart = part[i]-1
			# print(apart)
			mix_eigenvector.append(ovito[apart,:].tolist())
		mix_eigenvector = np.array(mix_eigenvector).reshape((-1,1)).astype(np.float)
		mix_eigenvector = np.abs(mix_eigenvector)
		print(mix_eigenvector.shape)
		l_xev = len(mix_eigenvector)

		max_vector = np.max(mix_eigenvector)
		min_vector = np.min(mix_eigenvector)

		scale = (max_vector-min_vector)/bar_number
		count = []
		for j in range(bar_number):
			count.append([])

		for i in range(l_xev):
			for j in range(bar_number):

				if mix_eigenvector[i]>=e:
					if mix_eigenvector[i]>=min_vector+scale*(j) and mix_eigenvector[i]<min_vector+scale*(j+1):
						count[j].append(mix_eigenvector[i].tolist())
						# print(mix_eigenvector[i])				
					else:
						pass


		Eigenvector_Amplitude = np.linspace(min_vector,max_vector,num=bar_number)
		
		len_count = []
		for j in range(bar_number):
			len_count.append(len(count[j]))

		print(Eigenvector_Amplitude,len_count)		

		return Eigenvector_Amplitude, len_count


	def part2count(self,bar_number):
		# 因为顺序一致，所以这里直接按照顺序来代替序号
		ovito = np.loadtxt(self.data,skiprows=2,usecols=(0,4,5,6),dtype=str)
		# print(ovito[:,0])
		mix_eigenvector = []
		for i in range(len(ovito)):
			if ovito[i,0] == "Se":
				mix_eigenvector.append(ovito[i,1:].tolist())
		mix_eigenvector = np.array(mix_eigenvector).reshape((-1,1)).astype(np.float)
		mix_eigenvector = np.abs(mix_eigenvector)
		print(mix_eigenvector.shape)
		
		l_xev = len(mix_eigenvector)

		max_vector = np.max(mix_eigenvector)
		min_vector = np.min(mix_eigenvector)

		scale = (max_vector-min_vector)/bar_number
		count = []
		for j in range(bar_number):
			count.append([])

		for i in range(l_xev):
			for j in range(bar_number):

				if mix_eigenvector[i]>=e:
					if mix_eigenvector[i]>=min_vector+scale*(j) and mix_eigenvector[i]<min_vector+scale*(j+1):
						count[j].append(mix_eigenvector[i].tolist())
						# print(mix_eigenvector[i])				
					else:
						pass


		Eigenvector_Amplitude = np.linspace(min_vector,max_vector,num=bar_number)
		
		len_count = []
		for j in range(bar_number):
			len_count.append(len(count[j]))

		print(Eigenvector_Amplitude,len_count)		

		return Eigenvector_Amplitude, len_count


	def plot(self,x,y,bar_width=0.001,dpi=300,Save=True):
		plt.rc('font', family='Times New Roman',size=26)
		# fig, ax = plt.subplots(figsize=(10, 8))
		# fig.subplots_adjust(bottom=0.2,left=0.2)
		fig = plt.figure(figsize=(10,8))
		fig.subplots_adjust(bottom=0.2,left=0.2)		
		'''打截断'''
		bax = brokenaxes(ylims=((0,80),(1100,1170)),hspace=0.06,despine=False)
		bax.bar(x, y, bar_width,hatch='\\\\',color='white',edgecolor='blue')

	
		# bax.set_xlabel('Eigenvector Amplitude',fontsize=26,fontweight='bold')
		# bax.set_ylabel('Count',fontsize=26,fontweight='bold')

		# bax.set_title('$\mathregular{\mathit{f}}$ =0.365THz')
		# plt.xticks([0,0.02,0.04,0.06,0.08,0.10,0.12],[0,0.02,0.04,0.06,0.08,0.10,0.12])
		# plt.yticks([0,200,400,600,800,1000,1200],[0,200,400,600,800,1000,1200])
		# plt.yticks([0,5,10,15,20],[0,5,10,15,20])
		# plt.yticks([0,2,4,6,8,10],[0,2,4,6,8,10])

		if Save==True:
 			plt.savefig(self.data+'.tiff',dpi=dpi)

		plt.show()
		return



if __name__ == '__main__':
	path = '../L0=5.40/Eigenvector/'
	ovitofile = '10Kpoint_0.365108_eigenvector32.dat'
	# ovitofile = '10Kpoint_0.324041_eigenvector78.dat'
	# ovitofile = '10Kpoint_0.255965_eigenvector209.dat'

	# 柱状图的柱子的数量
	bar_number = 50

	# 若本征矢小于e时，不count
	e = 0#0.01

	# 直方图宽度
	bar_width=0.001
	# Plot
	Save = True
	dpi=300

	c = CountEigenVector(path+ovitofile)

	# 1. 对所有本征矢计数
	x, y = c.count(bar_number,e)
	'''
	# 2. 只对一部分本征矢计数（MoSe2）
	# 需要计数的部分原子序号
	part = [118, 119, 120, 121, 122,123, 
			172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183,
			229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243,
			295, 296, 297, 298, 299, 300, 301, 302, 303, 
			361, 362, 363]
	x, y = c.part1count(part,bar_number)
	'''
	# 3. 只对一部分本征矢计数（MoSe2区域中Se原子）
	# x, y = c.part2count(bar_number)

	c.plot(x, y, bar_width, dpi,Save=True)