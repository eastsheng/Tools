# calculating the radial distribution function(RDF) from position lammpstrj info
import numpy as np
import re
import matplotlib.pyplot as plt
class RDFunction(object):
	"""read position information from lammpstrj"""
	def Info(self, lammpstrj,Ng=1000):
		self.lammpstrj = lammpstrj
		self.Number =  0#initalization of total atom number
		self.xlo = 0
		self.xhi = 0
		self.ylo = 0
		self.yhi = 0
		self.lx = 0 #size  x
		self.ly = 0 #size  y base on two dimension structures
		self.r_max = 0
		self.Ng = Ng
		self.dr = 0

		with open(self.lammpstrj,'r') as pos:
			posread = pos.read()
			# print(posread)
			self.Number = int(re.findall('ITEM: NUMBER OF ATOMS\n(.*?)\nITEM: BOX BOUNDS',posread)[0])
			print('Total atom number:',self.Number)
			vector = re.findall('pp pp pp\n(.*?)\nITEM: ATOMS id type',posread,re.S)[0].split()
			vector = np.array(vector).reshape(3,2).astype(np.float)
			# print(vector,type(vector),vector.shape)
			self.xlo = vector[0,0]
			self.xhi = vector[0,1]
			self.ylo = vector[1,0]
			self.yhi = vector[1,1]
			print('\nBox x,y position(angstrom):')
			print(self.xlo,self.xhi)
			print(self.ylo,self.yhi)
			self.lx = (self.xhi-self.xlo)/10 #unit angstrom
			self.ly = (self.yhi-self.ylo)/10
			print('\nBox x,y size(nm):',self.lx,self.ly)

			# maximum radius
			self.r_max = min(self.lx,self.ly)
			# print(self.r_max)
			# bin size
			self.dr = self.r_max/self.Ng
			# print(dr)

		return

	def Position(self,):
		self.list_trj = []
		self.trj_array = []
		self.r = []
		with open(self.lammpstrj,'r') as pos:
			for index, line in enumerate(pos):
				line = line.strip().split()
				# print(len(line))
				if len(line)==5:
					# print(line)
					self.list_trj.append(line)
			# print(type(len(self.list_trj)))
			self.trj_array = np.array(self.list_trj).reshape(-1,self.Number,5)
			# print(self.trj_array.shape,type(self.trj_array),len(self.trj_array))
			# print(self.trj_array)
			self.r = self.trj_array[:,:,2:4] #xy position every frame
			self.r = self.r.astype(np.float32)
			# print(self.r.shape,len(self.r),)
		return 

	def CalculateRDF(self,):
		self.rho = self.Number/(self.lx*self.ly)
		self.Rdf = np.zeros((self.Ng,1))
		self.lenz = len(self.r)

		L = np.array([self.lx,self.ly])
		pbc = np.array([1,1])
		LTimePBC = L*pbc

		for z in range(1,self.lenz+1):
			print('\nThe',str(z)+'th Frame')
			for i in range(1,self.Number-1):
				# print('Number of atom:',i)
				for j in range(i+1,self.Number): #skipping half of the pairs
					# print(self.r[z,j,:].dtype)
					rij = self.r[z,j,:] - self.r[z,i,:] #position difference vector
					rij = rij - np.around(rij/L)*LTimePBC 
					dij = np.sqrt(sum(rij*rij))   
					if dij < self.r_max:  #cutoff
						index = int(dij/self.dr) #bin index
						# print(index)
						self.Rdf[index] = self.Rdf[index]+1   #accumulate
						# print(self.Rdf)


		return 
		"""calculate g"""
	def Final(self,):

		for i in range(1,self.Ng+1):
			self.Rdf[i]/self.Number*2  #2 because half of the pairs have been skipped
			dV = 2*np.pi*(self.dr*i)*self.dr
			self.Rdf[i] = self.Rdf[i]/dV #now rdf is the local density
			self.Rdf[i] = self.Rdf[i]/self.rho #now rdf is the RDF

		return self.Rdf 

	def SavePlot(self,):
		r = range(1,self.Ng+1)*self.dr
		g = self.Rdf/self.lenz

		plt.plot(r,g,'o-')
		plt.show()
		return 


rdf = RDFunction()

rdf.Info('0nvt_1.lammpstrj')
rdf.Position()
rdf.CalculateRDF()
rdf.Final()
rdf.SavePlot()