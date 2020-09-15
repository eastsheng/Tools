# Average group velocity of a given frequency

import numpy as np
class GroupVelocity(object):
 	"""Read GroupVelocity array"""
 	def ReadVelocity(self,fvelocity_data):
 		self.data = np.loadtxt(fvelocity_data)
 		print('Size of Array:',self.data.shape)
 		return 

 	def FAverageV(self,frequency):
 		self.f = frequency
 		self.givenv = []
 		"""find average velocity of a given frequency"""
 		v_array=self.data
 		for i in range(len(v_array)):
 			# print(i)
 			if self.f == v_array[i,0]:
 				print('Frequency='+str(self.f),'Velocity='+str(v_array[i,1]))
 				self.givenv.append(v_array[i,1])
 		# print(self.givenv)
 		average_v = np.average(self.givenv)
 		print('Average group velocity at',self.f,'THz:\nVf=',average_v/1000,'km/s')
 		return

 	def AllFreAverageV(self,):
 		"""Whole frequency average velocity"""
 		v_array = self.data
 		aaverage_v = np.average(v_array[:,1])
 		print('Whole frequency average group velocity:\nVw=',aaverage_v/1000,'km/s')
 		return 

GV = GroupVelocity()
GV.ReadVelocity('phonon_group_velocity33.dat')
GV.FAverageV(0)
# GV.AllFreAverageV()