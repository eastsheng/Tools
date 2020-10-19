# create the xyz file from lammps data
import numpy as np
import re
# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)
class CreateXYZ(object):

	def readxyz(self,lammpsdata):
		with open(lammpsdata,'r') as rbox:
			for index,line in enumerate(rbox,1):
				if 'xlo xhi' in line:
					x = re.findall('    (.*?) xlo xhi',line)
				elif 'ylo yhi' in line:
					y = re.findall('    (.*?) ylo yhi',line)				
				elif 'zlo zhi' in line:
					z = re.findall('    (.*?) zlo zhi',line)
				elif 'Atoms #' in line:
					# print(index)
					skiprow= index
				else:
					pass
		x = x[0].split()
		y = y[0].split()
		z = z[0].split()
		box = np.array(x+y+z).reshape(3,2).astype(float)
		# print(box)
		self.L_x = box[0,1]-box[0,0]
		self.L_y = box[1,1]-box[1,0]
		self.L_z = box[2,1]-box[2,0]
		print('Length of X,Y,Z:',self.L_x,self.L_y,self.L_z)
		self.data = np.loadtxt(lammpsdata,skiprows=skiprow)
		self.N = len(self.data)
		print('Number of Total Atoms:',self.N)
		return

	def write_header(self,savedata,MN,cutoff,ot,has_velocity,number_of_grouping_methods,
					pbc_x,pbc_y,pbc_z):
		# self.line0 = np.array([self.N,MN,cutoff,ot,has_velocity,number_of_grouping_methods]).reshape(1,6)
		# self.line1 = np.array([pbc_x,pbc_y,pbc_z,self.L_x,self.L_y,self.L_z]).reshape(1,6)
		# self.line01 = np.vstack((self.line0,self.line1))
		# print(self.line01.shape)
		# print(self.line1)
		self.line01 = ' '.join([str(self.N),MN,cutoff,ot,has_velocity,number_of_grouping_methods,'\n'+
		pbc_x,pbc_y,pbc_z,str(self.L_x),str(self.L_y),str(self.L_z)])
		print('Header line 0 and 1:\n'+self.line01)
		return

	# has_velocity=0 & number_of_grouping_methods=0
	def writexyz_V1(self,savedata,M1=0,M2=0,M3=0):
		self.Natom_type = len(np.unique(self.data[:,2]))
		print('Number of Atom Type:',self.Natom_type)
		lendata = len(self.data)
		atom_type = (self.data[:,2]-1).reshape(lendata,1)
		atom_xyz = self.data[:,4:7]
		# print(atom_type.shape,atom_xyz.shape)
		atom_txyz = np.hstack((atom_type,atom_xyz))
		atom_m = []
		for i in range(lendata):
			if int(atom_txyz[i,0]) == 0:
				# print(atom_type[i])
				atom_m = np.append(atom_m,M1)
			elif int(atom_txyz[i,0]) == 1:
				atom_m = np.append(atom_m,M2)
			elif int(atom_txyz[i,0]) == 2:
				atom_m = np.append(atom_m,M3)
			else:
				print('Atom type error or overmuch!')

		atom_m = atom_m.reshape(lendata,1)
		# print(atom_m.shape)
		atom_txyzm = np.hstack((atom_txyz,atom_m))
		np.savetxt(savedata,atom_txyzm,fmt='%d %.9f %.9f %.9f %.9f',
			header=self.line01)
		return

# -----------Main Program----------- #
# The '#' shouldn't be included in the header of 'xyz.in', delete it by yourself
print('\n+--------------------------+')
####################Variables####################
# Mass(only support 1 to 3 types of atom)
# M1,M2,M3 = 32.064000,95.940000,0
M1,M2 = 32.064000,95.940000
# bourdary conditions
pbc_x,pbc_y,pbc_z = ['1','1','1']
# lammps data
lammpsdata = 'MoS2.data'
# save xyz.in
savedata = 'xyz.in'
# maximum number of neighbors 
MN = '3'
# initial cutoff distance used for building the neighbor list.
cutoff = '2.1'
# orthogonal(0) or triclinic(1) box
ot = '0'
# contain the initial velocities(has_velocity = 1)
has_velocity = '0'
# number of grouping methods
number_of_grouping_methods = '0'
####################Variables####################

xyz = CreateXYZ()
xyz.readxyz(lammpsdata)
xyz.write_header(savedata,MN,cutoff,ot,has_velocity,
				number_of_grouping_methods,pbc_x,pbc_y,pbc_z)
xyz.writexyz_V1(savedata,M1,M2)
print('+--------------------------+\n')