# frequency-energy sum
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

class FrequencyEnergy(object):
	"""FrequencyEnergy"""
	def Sort(self,fre_ener):

		self.fe = np.loadtxt(fre_ener)
		# sorting by the 1th column
		self.fe_sort = self.fe[np.argsort(self.fe[:,0])]
		# merging the same frequency
		self.f_new = np.unique(self.fe_sort[:,0])
		
		return

	def Compare(self,x1,x2,y1,y2):
		if x1 == x2:
			y = y1+y2
		return y


	def NewFE(self,):
		len_all = len(self.fe_sort)
		len_new = len(self.f_new)
		print(len_all,len_new)
		for i in range(len_new):
			for j in range(len_all):
				print(i,j)
		return

Q = FrequencyEnergy()
Q.Sort('fre_high_energy_0.dat')
Q.NewFE()