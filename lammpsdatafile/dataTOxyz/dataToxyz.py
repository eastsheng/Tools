# write xyz file from lammpsdata
import numpy as np
np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)
	
#read info from lammpsdata file
class LammpsData(object):
	def readAtominfo(self,lammpsdata):
		self.lammpsdata = lammpsdata
		with open(self.lammpsdata,'r') as data:
			for index, line in enumerate(data,1):
				if " atoms" in line:
					self.atom_number = int(line[:-6])

				if "Atoms # full" in line:
					self.xyz_index_min = index
				elif "Velocities" in line:
					self.xyz_index_max = index
					# print(self.xyz_index_min,self.xyz_index_max)

		return print("xyz index in ["+str(self.xyz_index_min)+", "+str(self.xyz_index_max)+"]")

	def readXYZ(self,):
		a = self.xyz_index_min
		b = self.xyz_index_max
		c = self.atom_number 
		xyz_array = np.loadtxt(self.lammpsdata,skiprows=a,max_rows=c)
		
		# print(self.xyz)
		return xyz_array

	def writeXYZfile(self,xyzdata,xyz_array):

		with open(xyzdata,'w') as xyzdata:
			xyzdata.write(str(self.atom_number)+'\n')
			xyzdata.write("Atoms. Timestep: 1000000\n")
			for i in range(self.atom_number):
				xyz_line=str(xyz_array[i,4:7]).lstrip('[').rstrip(']')
				if xyz_array[i,2] == 1:
					xyzdata.write('C '+xyz_line+' #C10\n')
				elif xyz_array[i,2] == 2:
					xyzdata.write('C '+xyz_line+' #C11\n')
				elif xyz_array[i,2] == 3:
					xyzdata.write('C '+xyz_line+' #C12\n')
				elif xyz_array[i,2] == 4:
					xyzdata.write('C '+xyz_line+' #C13\n')
				elif xyz_array[i,2] == 5:
					xyzdata.write('C '+xyz_line+' #C14\n')
				elif xyz_array[i,2] == 6:
					xyzdata.write('C '+xyz_line+' #C15\n')
				elif xyz_array[i,2] == 7:
					xyzdata.write('C '+xyz_line+' #C16\n')
				elif xyz_array[i,2] == 8:
					xyzdata.write('C '+xyz_line+' #C20\n')
				elif xyz_array[i,2] == 9:
					xyzdata.write('C '+xyz_line+' #C40\n')
				elif xyz_array[i,2] == 10:
					xyzdata.write('C '+xyz_line+' #C41\n')
				elif xyz_array[i,2] == 11:
					xyzdata.write('C '+xyz_line+' #C42\n')
				elif xyz_array[i,2] == 12:
					xyzdata.write('C '+xyz_line+' #C43\n')

				elif xyz_array[i,2] == 13:
					xyzdata.write('F '+xyz_line+' #F11\n')
				elif xyz_array[i,2] == 14:
					xyzdata.write('F '+xyz_line+' #F13\n')
				elif xyz_array[i,2] == 15:
					xyzdata.write('F '+xyz_line+' #F14\n')
				elif xyz_array[i,2] == 16:
					xyzdata.write('F '+xyz_line+' #F15\n')
				elif xyz_array[i,2] == 17:
					xyzdata.write('F '+xyz_line+' #F16\n')
				elif xyz_array[i,2] == 18:
					xyzdata.write('F '+xyz_line+' #F20\n')

				elif xyz_array[i,2] == 19:
					xyzdata.write('H '+xyz_line+' #H10\n')
				elif xyz_array[i,2] == 20:
					xyzdata.write('H '+xyz_line+' #H12\n')
				elif xyz_array[i,2] == 21:
					xyzdata.write('H '+xyz_line+' #H16\n')					
				elif xyz_array[i,2] == 22:
					xyzdata.write('H '+xyz_line+' #H41\n')
				elif xyz_array[i,2] == 23:
					xyzdata.write('H '+xyz_line+' #H42\n')
				elif xyz_array[i,2] == 24:
					xyzdata.write('H '+xyz_line+' #H43\n')

				elif xyz_array[i,2] == 25:
					xyzdata.write('N '+xyz_line+' #N20\n')					

				elif xyz_array[i,2] == 26:
					xyzdata.write('Na '+xyz_line+' #Na30\n')

				elif xyz_array[i,2] == 27:
					xyzdata.write('O '+xyz_line+' #O20\n')
				elif xyz_array[i,2] == 28:
					xyzdata.write('O '+xyz_line+' #O40\n')
				elif xyz_array[i,2] == 29:
					xyzdata.write('O '+xyz_line+' #O41\n')

				elif xyz_array[i,2] == 30:
					xyzdata.write('S '+xyz_line+' #S20\n')
		return

# ---main program--- #

Ld = LammpsData()
if __name__ == '__main__':
	print("\n------Start!------\n")

	# input data
	lammpsdata = "aaa13.data"
	# output xyz
	xyzdata = 'aaa13.xyz'
	# read atom info from data
	atom_number = Ld.readAtominfo(lammpsdata)
	xyz_array = Ld.readXYZ()
	Ld.writeXYZfile(xyzdata,xyz_array)

	print("\n------Done!------\n")