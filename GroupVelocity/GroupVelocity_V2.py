# Average group velocity of a given frequency
import numpy as np
import matplotlib.pyplot as plt
class GroupVelocity(object):
 	"""Read GroupVelocity array"""
 	def ReadVelocity(self,fvelocity_data):
 		self.filename = fvelocity_data
 		self.data = np.loadtxt(self.filename)
 		self.mkm = 1000
 		f = self.data[:,0] #THz
 		v = self.data[:,1]/self.mkm #km/s
 		print('Size of Array:',self.data.shape)
 		return f,v

 	def FAverageV(self,frequency):
 		self.f = frequency
 		self.givenv = []
 		"""find average velocity of a given frequency"""
 		v_array=self.data
 		for i in range(len(v_array)):
 			# print(i)
 			if self.f == v_array[i,0]:
 				print('Frequency='+str(self.f),'Velocity='+str(v_array[i,1]/self.mkm),'km/s')
 				self.givenv.append(v_array[i,1])
 		# print(self.givenv)
 		average_v = np.average(self.givenv)
 		print('\nAverage group velocity at',self.f,'THz:\nVf=',average_v/self.mkm,'km/s\n')
 		return

 	def AllFreAverageV(self,):
 		"""Whole frequency average velocity"""
 		v_array = self.data
 		aaverage_v = np.average(v_array[:,1])
 		print('Whole frequency average group velocity:\nVw=',aaverage_v/self.mkm,'km/s')
 		return 

 	def RangeFre(self,fmin,fmax):
 		"""Average velocity of a given frequency range"""
 		v_array=self.data
 		list_range = []
 		for i in range(len(v_array)):
 			# print(i)
 			if v_array[i,0]>=fmin and v_array[i,0]<=fmax:
 				print('Frequency='+str(v_array[i,0]),'Velocity='+str(v_array[i,1]/self.mkm),'km/s')
 				list_range.append(v_array[i,1])

 		average_v = np.average(list_range)
 		print('Frequency in','['+str(fmin)+','+str(fmax)+']',average_v/self.mkm,'km/s')
 		return 	

 	def TotVelocity(self):
 		tot_v = np.sum(self.data[:,1])
 		print("\nThe sum of total velocities=",tot_v/self.mkm,"km/s\n")
 		return tot_v

 	def PlotGV(self,Plot=True,Save=True,dpi=300,fremin=0,fremax=16):
 		f = self.data[:,0] #THz
 		v = self.data[:,1]/self.mkm #km/s

 		plt.rc('font', family='Times New Roman', size=20)
 		fig,ax = plt.subplots(figsize=(8,6))
 		fig.subplots_adjust(bottom=0.2,left=0.2)

 		plt.scatter(f,v,color='b',marker='x',s=1)
 		ax.set_xlabel('Frequency (THz)',fontsize=26,fontweight='bold')
 		ax.set_ylabel('Group velocity (km/s)',fontsize=26,fontweight='bold')
 		plt.xticks(size=25)
 		plt.yticks(size=25)
 		plt.xlim(fremin,fremax)
 		plt.ylim(0,)
 		if Save==True:
 			plt.savefig(self.filename+'.tiff',dpi=dpi) 

 		if Plot==True:
 			plt.show()

 		plt.close()
 		return

 	def PlotTogether(self,f1,v1,f2,v2,f3,v3,Plot=True,Save=True,dpi=300,fremin=0,fremax=16,vmin=0,vmax=1):

 		plt.rc('font', family='Times New Roman', size=20)
 		fig,ax = plt.subplots(figsize=(8,6))
 		fig.subplots_adjust(bottom=0.2,left=0.2)

 		s1 = plt.scatter(f1,v1,color='r',marker='s',s=5)
 		s2 = plt.scatter(f2,v2,color='b',marker='^',s=5)
 		s3 = plt.scatter(f3,v3,color='c',marker='*',s=5)

 		plt.legend((s1,s2,s3),('$\mathregular{MoS_2}$/$\mathregular{MoSe^{32}}_\mathregular{2}$',
 								'$\mathregular{MoS_2}$/$\mathregular{MoSe^{78}}_\mathregular{2}$',
 								'$\mathregular{MoS_2}$/$\mathregular{MoSe^{209}}_\mathregular{2}$') ,loc = 'best')

 		ax.set_xlabel('Frequency (THz)',fontsize=26,fontweight='bold')
 		ax.set_ylabel('Group velocity (km/s)',fontsize=26,fontweight='bold')
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

pgv = 'phonon_group_velocity.dat'

# Plot
Plot=True
Save=True
dpi=300
# THz range
fremin, fremax = [0, 16]
# velocity range
vmin, vmax = [0, 0.6]

if __name__ == '__main__':

	GV = GroupVelocity()
	f1,v1=GV.ReadVelocity(path1+pgv)
	f2,v2=GV.ReadVelocity(path2+pgv)	
	f3,v3=GV.ReadVelocity(path3+pgv)
	GV.PlotTogether(f1, v1, f2, v2, f3, v3, Plot, Save, dpi, fremin, fremax, vmin, vmax)

# other functions
	# GV.ReadVelocity(path1+pgv)

	# # Average velocity of a given frequency
	# GV.FAverageV(0)

	# # Average velocity of whole frequency
	# GV.AllFreAverageV()

	# # Average velocity of a given frequency range
	# GV.RangeFre(0,2)

	# # The sum of all velocities
	# GV.TotVelocity()
	# GV.PlotGV(Plot,Save,dpi,fremin,fremax)


