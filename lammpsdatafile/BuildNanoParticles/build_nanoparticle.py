# build nanoparticle with different diameters from a lammps data file with the diameter of 5nm
# lammps data for nanoparticles writen by Dongsheng Chen, 2022/10/13

import numpy as np
import os
class BuildNPs(object):
 	"""docstring for BuildNPs"""
 	def __init__(self, lammps_data):
 		super(BuildNPs, self).__init__()
 		self.lammps_data = lammps_data
 	
 	def read_index(self):
 		with open(self.lammps_data,"r") as f:
 			for index, line in enumerate(f,1):
 				if "atoms" in line:
 					self.atom_number = int(line.split()[0])
 				if "Atoms # " in line:
 					self.data_full_index = index+1
 				if "xlo xhi" in line:
 					self.xlo = float(line.split()[0])
 					self.xhi = float(line.split()[1])
 				if "ylo yhi" in line:
 					self.ylo = float(line.split()[0])
 					self.yhi = float(line.split()[1])
 				if "zlo zhi" in line:
 					self.zlo = float(line.split()[0])
 					self.zhi = float(line.split()[1])

 	def find_cube_data(self,diameter=7):
 		full_data = np.loadtxt(self.lammps_data,skiprows=self.data_full_index,max_rows=self.atom_number)
 		m,n = full_data.shape
 		# find the position of center atom
 		ca = 0.5*(self.xhi+self.xlo)
 		cb = 0.5*(self.yhi+self.ylo)
 		cc = 0.5*(self.zhi+self.zlo) 
 		cube_center_position = [ca,cb,cc]
 		print("Center of cube is",cube_center_position)
 		radius = diameter*0.5
 		nanoNPs_list = []
 		error = 1e-5
 		for i in range(m):
 			if abs(full_data[i,4]-ca)-radius<=error and \
 			   abs(full_data[i,5]-cb)-radius<=error and \
 			   abs(full_data[i,6]-cc)-radius<=error:
 				# print(i)
 				nanoNPs_list.append(full_data[i,:])
 		nanoNPs_array = np.array(nanoNPs_list).reshape(-1,n)
 		self.mm,nn = nanoNPs_array.shape
 		count = 0
 		for i in range(self.mm):
 			nanoNPs_array[i,0] = i+1
 			if nanoNPs_array[i,2] == 1:
 				count = count + 1
 		np.savetxt("data_full.dat",nanoNPs_array,fmt="%d %d %d %f %f %f %f %d %d %d")	
 		self.minx, self.maxx = min(nanoNPs_array[:,4]), max(nanoNPs_array[:,4])	
 		self.miny, self.maxy = min(nanoNPs_array[:,5]), max(nanoNPs_array[:,5])	
 		self.minz, self.maxz = min(nanoNPs_array[:,6]), max(nanoNPs_array[:,6])
 		# print(nanoNPs_array.shape)
 		print("Total number of atom =",self.mm)
 		print("Number of atom 1 =",count)
 		print("Number of atom 2 =",self.mm-count)

 	def find_circle_data(self,diameter=7,center_factor=[0.51,0.5,0.5]):
 		full_data = np.loadtxt(self.lammps_data,skiprows=self.data_full_index,max_rows=self.atom_number)
 		m,n = full_data.shape
 		# find the position of center atom
 		ca = center_factor[0]*(self.xhi+self.xlo)
 		cb = center_factor[1]*(self.yhi+self.ylo)
 		cc = center_factor[2]*(self.zhi+self.zlo) 
 		cube_center_position = [ca,cb,cc]
 		print("Center of cube is",cube_center_position)
 		radius = diameter*0.5
 		nanoNPs_list = []
 		error = 1e0
 		for i in range(m):

 			ra = full_data[i,4]-ca
 			rb = full_data[i,5]-cb
 			rc = full_data[i,6]-cc
 			r = np.sqrt(ra**2+rb**2+rc**2)
 			if r - radius<=error:
 				# print(i)
 				nanoNPs_list.append(full_data[i,:])
 		nanoNPs_array = np.array(nanoNPs_list).reshape(-1,n)
 		self.mm,nn = nanoNPs_array.shape
 		count = 0
 		for i in range(self.mm):
 			nanoNPs_array[i,0] = i+1
 			if nanoNPs_array[i,2] == 1:
 				count = count + 1
 		np.savetxt("data_full.dat",nanoNPs_array,fmt="%d %d %d %f %f %f %f %d %d %d")	
 		self.minx, self.maxx = min(nanoNPs_array[:,4]), max(nanoNPs_array[:,4])	
 		self.miny, self.maxy = min(nanoNPs_array[:,5]), max(nanoNPs_array[:,5])	
 		self.minz, self.maxz = min(nanoNPs_array[:,6]), max(nanoNPs_array[:,6])
 		# print(nanoNPs_array.shape)
 		print("Total number of atom =",self.mm)
 		print("Number of atom 1 =",count)
 		print("Number of atom 2 =",self.mm-count)

 	def write_data(self,Npsdata):
 		with open(Npsdata,"w") as nps:
 			nps.write("LAMMPS data file for nanoparticles writen by Dongsheng Chen, 2022/10/13\n\n")
 			nps.write("\t"+str(self.mm)+" atoms\n")
 			nps.write("\t2 atom types\n\n")
 			nps.write("\t"+str(self.minx)+"\t"+str(self.maxx)+"\txlo xhi\n")
 			nps.write("\t"+str(self.miny)+"\t"+str(self.maxy)+"\tylo yhi\n")
 			nps.write("\t"+str(self.minz)+"\t"+str(self.maxz)+"\tzlo zhi\n\n")
 			nps.write("Masses\n\n")
 			nps.write("\t1 28.086 # Si1\n")
 			nps.write("\t2 28.086 # Si2\n\n")
 			nps.write("Pair Coeffs # lj/cut/coul/long\n\n")			
 			nps.write("\t1\t0.01\t3.95 # Si1\n")			
 			nps.write("\t2\t0.01\t3.95 # Si2\n\n") 			
 			nps.write("Atoms # full\n\n")
 			for line in open("data_full.dat"):
 				nps.writelines(line)
 		os.remove("data_full.dat")
 		return



if __name__ == '__main__':
	lammps_data = "Si_Crystal_5nm.data"
	diameter = 20 # Diameter/Angstrom
	bn = BuildNPs(lammps_data)
	bn.read_index()
	# bn.find_cube_data(diameter)
	bn.find_circle_data(diameter,center_factor = [0.475,0.5,0.5])
	bn.write_data("JanusNPs_"+str(diameter)+"A.data")