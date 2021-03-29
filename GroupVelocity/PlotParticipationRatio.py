# Average group velocity of a given frequency
import numpy as np
import matplotlib.pyplot as plt
class ParticipationRatio(object):
 	"""Read Participation Ratio array"""
 	def readdata(self,fvelocity_data):
 		self.filename = fvelocity_data
 		self.data = np.loadtxt(self.filename)
 		x = self.data[:,0] #THz
 		y = self.data[:,1]#/self.mkm #km/s
 		print('Size of Array:',self.data.shape)
 		return x,y	

 	def PlotTogether(self,f1,v1,f2,v2,f3,v3,Plot=True,Save=True,dpi=300,fremin=0,fremax=16,vmin=0,vmax=1):

 		plt.rc('font', family='Times New Roman', size=20)
 		fig,ax = plt.subplots(figsize=(8,6))
 		fig.subplots_adjust(bottom=0.2,left=0.2)

 		s1 = plt.scatter(f1,v1,color='r',marker='s',s=5)
 		s2 = plt.scatter(f2,v2,color='b',marker='^',s=5)
 		s3 = plt.scatter(f3,v3,color='c',marker='*',s=5)

 		leg = plt.legend((s1,s2,s3),('$\mathregular{MoS_2}$/$\mathregular{MoSe^{32}}_\mathregular{2}$',
 							 	'$\mathregular{MoS_2}$/$\mathregular{MoSe^{78}}_\mathregular{2}$',
 								'$\mathregular{MoS_2}$/$\mathregular{MoSe^{209}}_\mathregular{2}$'),
 								loc = 'upper center',fontsize=16)

 		ax.set_xlabel('Frequency (THz)',fontsize=26,fontweight='bold')
 		ax.set_ylabel('Participation Ratio',fontsize=26,fontweight='bold')
 		plt.xticks([0,2,4,6,8,10,12,14,16],[0,2,4,6,8,10,12,14,16],size=25)
 		plt.yticks(size=25)
 		plt.xlim(fremin,fremax)
 		plt.ylim(vmin,vmax)
 		if Save==True:
 			plt.savefig(self.filename+'.tiff',dpi=dpi) 

 		if Plot==True:
 			plt.show()

 		plt.close()
 		return


path1 = '../L0=5.40/Se32/'
path2 = '../L0=5.40/Se78/'
path3 = '../L0=5.40/Se209/'

pgv = 'participation_ratio.dat'

# Plot
Plot=True
Save=True
dpi=300
# THz range
fremin, fremax = [0, 16]
# PR range
ymin, ymax = [0, 1.0]

if __name__ == '__main__':

	PR = ParticipationRatio()
	x1,y1=PR.readdata(path1+pgv)
	x2,y2=PR.readdata(path2+pgv)	
	x3,y3=PR.readdata(path3+pgv)
	PR.PlotTogether(x1, y1, x2, y2, x3, y3, Plot, Save, dpi, fremin, fremax, ymin, ymax)
