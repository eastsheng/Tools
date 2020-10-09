# DEAL AND PLOT THE DISPERSION FROM 'GULP' PACKAGE
import numpy as np 
import matplotlib.pyplot as plt
class GulpDisp(object):
	"""Gulp Dispersion"""
	def Readata(self,disp_data,number_atom=96):
		self.disp_data = disp_data
		self.number_branch=number_atom*3
		return 

	def Plot(self,xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True):
		self.data = np.loadtxt(self.disp_data)
		print(self.data.shape)
		# print(self.data)
		# print(len(self.data))
		len_data = len(self.data)
		line_number = int(len_data/self.number_branch)
		WaveVector = np.linspace(0,1,line_number)
		Frequency = self.data[:,1].reshape((line_number,self.number_branch))
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
number_atom = 240
# plot x y range and line width
xmin,xmax = [0,1]
ymin,ymax = [0,2]
linewidth = 2

gulp = GulpDisp()
# gulp.ReadKpoint('C3NGRAdispersion.disp',number_atom)
gulp.Readata('20_5x8_S209.disp',number_atom)
gulp.Plot(xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True)
