# frequency-energy sum
import numpy as np
import itertools
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

class FrequencyEnergy(object):
	"""FrequencyEnergy"""
	def Sort(self,fre_ener,Round=2):
		data = np.loadtxt(fre_ener)
		# print(data.shape,type(data))
		length = len(data)
		self.frequency = np.around(data[:,0],Round).reshape(length,1)
		self.energy = data[:,1].reshape(length,1)
		fe = np.hstack((self.frequency,self.energy))
		# Sorting by 1th column of fe array
		self.fe_sort = fe[np.argsort(fe[:,0])] 
		# print(self.frequency.shape,self.energy.shape)
		# print(self.fe_sort.shape)
		return

	def SumByFSF(self):
		"""Merging the energies of same frequencies"""
		new_fe = [(sum(i[1] for i in group), key) for key, 
		group in itertools.groupby(sorted(self.fe_sort, 
			key = lambda i: i[0]), lambda i: i[0])]
		# print(type(new_fe),new_fe)
		new_fe = np.array(new_fe)
		print(new_fe.shape)
		new_length = len(new_fe)

		self.new_frequency = new_fe[:,1].reshape(new_length,1)
		self.new_energy = new_fe[:,0].reshape(new_length,1)
		self.new_fe = np.hstack((self.new_frequency,self.new_energy))
		# Normalized energy
		# max_energy = np.max(self.new_energy)
		max_energy = 22.489789999999996
		if max_energy != 0:
			Normalized_energy = self.new_energy/max_energy
		else:
			Normalized_energy = self.new_energy
		self.normalized_fe = np.hstack((self.new_frequency,Normalized_energy))
		print('Max energy=',max_energy)			
		return


	def SavePlot(self,savefe,Normalized=True):
		# print(self.new_fe)
		if Normalized==False:
			np.savetxt(savefe,self.new_fe,fmt='%f %f')
		elif Normalized==True:
			np.savetxt(savefe,self.normalized_fe,fmt='%f %f')
		plt.plot(self.new_frequency,self.new_energy)
		# plt.show()
		return


i = 0
# variable = 'separate'
Normalized=True


Q = FrequencyEnergy()
Q.Sort('high_energy_'+str(i)+'.dat',Round=1)
Q.SumByFSF()
# Q.SavePlot(variable+'new_fre_high_energy_'+str(i)+'.dat',Normalized)
Q.SavePlot('new_high_energy_'+str(i)+'.dat',Normalized)
