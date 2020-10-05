# DEAL AND PLOT THE DISPERSION FROM 'GULP' PACKAGE
import numpy as np 
import re
import matplotlib.pyplot as plt
class GulpDisp(object):
	"""Gulp Dispersion"""
	def Read(self,disp_data,number_atom=96):
		self.disp_data = disp_data
		self.K = 0
		self.number_atom=number_atom
		with open(disp_data,'r')as disp:
			for line in disp:
				if 'Final K point' in line:
					# print(line)
					K =re.findall('K point =   (.*?)  ',line)[0]
					self.K = float(K)
					print('\nk Point path =','[ 0 ,',str(self.K),']\n')
				else:
					pass
		return

	def Plot(self,xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True):
		self.data = np.loadtxt(self.disp_data)
		print(self.data.shape)
		# print(self.data)
		# print(len(self.data))
		len_data = len(self.data)
		line_number = int(len_data/self.number_atom)
		
		WaveVector = self.K*(np.unique(self.data[:,0]-1)/(len_data/line_number))
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

# Main Program
number_atom = 96

# plot
xmin,xmax = [0,0.5]
ymin,ymax = [0,2]
linewidth = 2

gulp = GulpDisp()
gulp.Read('C3NGRAdispersion.disp',number_atom)
gulp.Plot(xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True)
