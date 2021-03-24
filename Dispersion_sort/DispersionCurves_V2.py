# deal data and plot dispersion curves
import numpy as np
import matplotlib.pyplot as plt

class Dispersion(object):
	def phonon_sort(self,k_point,filename1,filename2):
		self.k_point = k_point # k_point = 50#k_point数
		self.filename1 = filename1
		self.filename2 = filename2
		self.cm2THz = 33.36    # 单位转换1THz=33.36cm-1,如果频率已经是THz，修改为1
		self.number_round = 6  # 保留6位有效数字
		with open(self.filename1) as sort_before, open(self.filename2, 'w') as p_sort_after:
			sort = sort_before.read().strip().split()
			# print(sort)
			sort = map(eval,sort)
			sort = list(sort)
			print('总元素数：',len(sort))
			row_number = int(len(sort)/self.k_point)  # 原本每一行数字的数量,原子数*3，
			print('\n每一行元素数：',row_number,'个数据，其中前三个是基矢\n')#可能多了一列，在第四列全是0.删掉
			atom_number = int((row_number-3)/3)
			print('原子个数：',atom_number)
			# 由于输出的格式不正确，这里是修改格式
			for i in range(self.k_point):
				# print(i)
				for j in range(i*row_number,(i+1)*row_number):
					# print(sort[j])
					# print(j)
					sortly = round(sort[j],6)
					if self.cm2THz == 33.36:
						sortly = str(sortly/self.cm2THz)#注意数据单位修改
					else:
						sortly = sortly
					p_sort_after.write(sortly)
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

		data = np.loadtxt(self.filename2)
		print(data.shape)
		if self.cm2THz == 33.36:
			print('注：\n“如果数据没有转换单位到THz,需要在此程序转换”')
			# 由于之前在转换单位的时候把基矢也转换了，所以在此把基矢*33.36
			vector = data[:,0]*33.36
			# print(vector)
		else:
			vector = data[:, 0]
		frequency = data[:, 4:]#由于多出第一列位移，2 3 4 列是波矢，所以从第5列开始是频率
		# print(frequency)
		
		plt.rc('font', family='Times New Roman', size=20)
		fig, ax = plt.subplots(figsize=(self.figsx, self.figsy))
		fig.subplots_adjust(bottom=0.1,left=0.2)
		plt.plot(vector,frequency,'blue',linewidth=lw)
		# 格式
		# plt.title('Dipersion', size=26)
		ax.set_xlabel('Wave vector',fontsize=32)#,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=32)
		plt.xticks(size=25)
		plt.yticks(size=25)
		# 范围
		plt.xlim(self.r_xmin, self.r_xmax)
		plt.ylim(self.r_ymin, self.r_ymax)
		# 保存
		plt.savefig(self.figname, dpi=self.figdpi)
		plt.show()
		plt.close()
		return 



k_point = 50
# 图片大小,默认为(8,6),dpi=300
figsize_x = 8
figsize_y = 16
dpi = 300
# 线宽默认为1.0
lw = 1.0
# 画图范围，默认x:(0,0.5),y:(0,2)
range_xmin = 0
range_xmax = 0.5
range_ymin = 0
range_ymax = 2
# 原始需要分类的dipersion文件
disper_before = './33_3x8/phonon_sorted.dat'
# 要保存的文件
disper_after = './33_3x8/p_sorted_33'

# 保存的图片
disperfig = './33_3x8/phonon_disp33.tiff'

dispersion = Dispersion()
dispersion.phonon_sort(k_point, disper_before, disper_after)
dispersion.plot_curves(disperfig, dpi, lw,
                       figsize_x, figsize_y,
                       range_xmin, range_xmax,
                       range_ymin, range_ymax)
