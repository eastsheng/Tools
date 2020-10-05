# DEAL AND PLOT THE DISPERSION FROM 'GULP' PACKAGE
import numpy as np 
import re
import matplotlib.pyplot as plt
class GulpDisp(object):
	"""Gulp Dispersion"""
	def Readata(self,disp_data,number_atom=96):
		self.disp_data = disp_data
		self.number_atom=number_atom
		return 

	def Kpoint(self,number_path,GammatoX=True):
		self.K = 0
		self.GammatoX = GammatoX
		self.number_path = number_path
		if GammatoX==True:
			with open(self.disp_data,'r')as disp:
				for line in disp:
					if 'Start K point' in line:
						# print(line)
						K =re.findall('K point =   (.*?)  ',line)[0]
						self.K = float(K)
						print('\nk Point path =','[ 0 ,',str(self.K),']\n')
					else:
						pass
		else:
			print('There are "'+str(self.number_path)+'" Brillouion paths')
		return

	def Plot(self,xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True):
		self.data = np.loadtxt(self.disp_data)
		print(self.data.shape)
		# print(self.data)
		# print(len(self.data))
		len_data = len(self.data)
		line_number = int(len_data/self.number_atom)
		if self.GammatoX == True:
			WaveVector = self.K*(np.unique(self.data[:,0]-1)/(len_data/line_number))
		else:
			WaveVector = np.linspace(0,1,line_number)
		Frequency = self.data[:,1].reshape((line_number,self.number_atom))
		Frequency = Frequency/33.36 # CM-1 >> THz
		
		# print(Frequency.shape)

		# Plot
		plt.rc('font',family='Times New Roman',size=16)
		fig,ax = plt.subplots(figsize = (6,8))
		fig.subplots_adjust(bottom=0.1,left=0.2)
		plt.plot(WaveVector,Frequency,'b',linewidth=linewidth)
		ax.set_xlabel('Wave Vector',fontsize=32,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=32)
		plt.xlim(xmin,xmax)
		plt.ylim(ymin,ymax)
		if save == True:
			plt.savefig('fig.png',dpi=dpi)
		plt.show()

		return 

# *************Main Program************* #
# The number of atoms in the primitive cell
number_atom = 720
# plot x y range and line width
xmin,xmax = [0,1]
ymin,ymax = [0,2]
linewidth = 2
# whether the brillouion zone path from Gamma to X 
GammatoX=False
# How many paths?
number_path  = 2

gulp = GulpDisp()
# gulp.ReadKpoint('C3NGRAdispersion.disp',number_atom)
gulp.Readata('20_5x8_S209.disp',number_atom)
gulp.Kpoint(number_path,GammatoX,)
gulp.Plot(xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True)
