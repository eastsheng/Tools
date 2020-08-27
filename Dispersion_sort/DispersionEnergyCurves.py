# deal data and plot dispersion curves
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

class Dispersion(object):
	def phonon_sort(self,k_point,filename1,filename2,cm2THz=33.36):
		self.k_point = k_point # k_point = 50#k_point数
		self.filename1 = filename1
		self.filename2 = filename2
		self.cm2THz = cm2THz   # 单位转换1THz=33.36cm-1,如果频率已经是THz，修改为1
		self.number_round = 6  # 保留6位有效数字
		self.atom_number=0
		with open(self.filename1) as sort_before, open(self.filename2, 'w') as p_sort_after:
			sort = sort_before.read().strip().split()
			# print(sort)
			sort = map(eval,sort)
			sort = list(sort)
			print('总元素数：',len(sort))
			row_number = int(len(sort)/self.k_point)  # 原本每一行数字的数量,原子数*3，
			print('\n每一行元素数：',row_number,'个数据，其中第一个是位移，接着三个是基矢，接着是频率和能量\n')
			self.atom_number = int((row_number-4)/6)#，因为能量的列数与频率相同，所以由/3，改成/6
			print('原子个数：',self.atom_number)
			# 由于输出的格式不正确，这里是修改格式
			for i in range(self.k_point):
				# print(i)
				for j in range(i*row_number,(i+1)*row_number):
					# print(sort[j])
					# print(j)
					sortly = round(sort[j],self.number_round)
					if self.cm2THz == 33.36:
						sortly = str(sortly/self.cm2THz)#注意数据单位修改
					else:
						sortly = sortly
					p_sort_after.write(str(sortly))
					# p_sort_after.write(str(sortly))
					p_sort_after.write(3*'\t')
				p_sort_after.write('\n')

			return 
	def plot_curves(self, figname, dpi=300,lw=1.0, figsize_x=8, figsize_y=16, 
                 rxmin=0, rxmax=0.5, rymin=0, rymax=2):
		self.figname = figname
		self.figdpi = dpi 
		self.linewidth = lw
		self.figsx = figsize_x
		self.figsy = figsize_y
		self.r_xmin = rxmin  # range of x
		self.r_xmax = rxmax
		self.r_ymin = rymin  # range of y
		self.r_ymax = rymax
		self.vector = 0
		self.frequency = 0
		self.energy = 0
		self.energymin = 0
		self.energymax = 0

		data = np.loadtxt(self.filename2)
		print(data.shape)
		if self.cm2THz == 33.36:
			print('注：\n“如果数据没有转换单位到THz,需要在此程序转换”')
			# 由于之前在转换单位的时候把基矢也转换了，所以在此把基矢*33.36
			self.vector = data[:,0]*33.36
			# print(vector)
			self.energy = data[:,self.atom_number*3+4:]*33.36
		else:
			self.vector = data[:,0]
			self.energy = data[:,self.atom_number*3+4:]

		self.frequency = data[:, 4:self.atom_number*3+4]#由于多出第一列位移，2 3 4 列是波矢，所以从第5列开始是频率
		self.energymin = self.energy.min()
		self.energymax = self.energy.max()
		print(self.energymin,self.energymax)
		print(self.frequency.shape)
		print(self.energy.shape)

		plt.rc('font', family='Times New Roman', size=16)
		plt.figure(figsize=(self.figsx, self.figsy))
		plt.plot(self.vector,self.frequency,'b',linewidth=self.linewidth)
		# 格式
		# plt.title('Dipersion', size=26)
		plt.xlabel('Wave vector',size=22)
		plt.ylabel('Frequency (THz)',size=22)		
		plt.xticks(size=22)
		plt.yticks(size=22)
		# 范围
		plt.xlim(self.r_xmin, self.r_xmax)
		plt.ylim(self.r_ymin, self.r_ymax)
		# 保存
		plt.savefig(self.figname, dpi=self.figdpi)
		# plt.show()
		plt.close()
		return 

	def plot_energy(self,figname_energy):
		self.figname_energy = figname_energy

		vector = self.vector.reshape((self.k_point,1))

		plt.rc('font', family='Times New Roman', size=20)
		# fig = plt.figure(figsize=(self.figsx, self.figsy))
		# axs = fig.add_subplot(1,1,1)
		fig, ax = plt.subplots(figsize=(self.figsx, self.figsy))
		fig.subplots_adjust(bottom=0.1,left=0.2)

		for i in range(self.atom_number*3):
			# print(i)
			frequency = self.frequency[:,i].reshape((self.k_point,1))
			energy = self.energy[:,i]

			points = np.array([vector,frequency]).T.reshape(-1, 1, 2)
			segments = np.concatenate([points[:-1], points[1:]], axis=1)

			# norm = plt.Normalize(self.energymin,self.energymax)#最大最小值
			norm = plt.Normalize(0.0002,0.8)

			lc = LineCollection(segments, cmap='jet', norm=norm)
			lc.set_array(energy)
			lc.set_linewidth(self.linewidth)
			line = ax.add_collection(lc)
		fig.colorbar(line)
		# 格式
		# plt.title('Dipersion', size=26)
		ax.set_xlabel('Wave vector',fontsize=32,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=32)
		# plt.xlabel('Wave vector',size=32)
		# plt.ylabel('Frequency (THz)',size=32)		
		plt.xticks(size=25)
		plt.yticks(size=25)
		# 范围
		plt.xlim(self.r_xmin, self.r_xmax)
		plt.ylim(self.r_ymin, self.r_ymax)
		# 保存
		plt.savefig(self.figname_energy, dpi=self.figdpi)
		plt.show()
		plt.close()

		return




k_point = 50
# 图片大小,默认为(8,6),dpi=300
figsize_x = 8
figsize_y = 16
dpi = 300
# 线宽默认为1.0
lw = 4
# 画图范围，默认x:(0,0.5),y:(0,2)
range_xmin = 0
range_xmax = 0.5
range_ymin = 0
range_ymax = 2.0
# 原始需要分类的dipersion文件
# disper_before = 'phonon_sorted.dat'
disper_before_ener = 'phonon_sorted_energy209.dat'
# 要保存的文件
# disper_after = 'p_sorted'
disper_after_ener = 'p_sorted_energy209'

# 保存的图片
disperfig = 'phonon_disp209.tiff'
disperEnergyfig = 'phonon_dispEnergy209.tiff'

dispersion = Dispersion()
dispersion.phonon_sort(k_point, disper_before_ener, disper_after_ener)
dispersion.plot_curves(disperfig, dpi, lw,
                       figsize_x, figsize_y,
                       range_xmin, range_xmax,
                       range_ymin, range_ymax)

dispersion.plot_energy(disperEnergyfig)