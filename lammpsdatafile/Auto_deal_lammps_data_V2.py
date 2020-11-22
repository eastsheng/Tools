#Process the data from msi2lmp for lammps full or atoms
import numpy as np

class LAMMPSData(object):
	def ToFull(self,filename1,filename2,type_p):
		self.filename2=filename2
		self.skiprow = 0
		with open(filename1,'r')as data1,open(filename2,'w')as data2:
			for index, line in enumerate(data1,1):
				line_ss = line.strip().split()
				line_len = len(line_ss)
				# print(line)
				
				if index == 1:#header
					data2.write(line)

				if line_len == 2 and line_ss[1]=='atoms':#number atoms
					print(line)
					data2.write(line)
					data2.write('\n')
				if line_len == 3 and line_ss[1]=='atom':#atom types
					data2.write(line)
					data2.write('\n')
				if line_len == 4 and line_ss[2] in ['xlo','ylo','zlo']:#position
					data2.write(line)
				if line == 'Masses\n':
					data2.write('\n')
					data2.write(line)
					data2.write('\n')
				if line_len == 4 and line_ss[2]=='#' and line_ss[1]!='Coeffs':
					data2.write(line)

				if line=='Atoms # full\n':
					self.skiprow=index
					data2.write('\n')
					data2.write(line)
					data2.write('\n')
				# if the data is relaxed, the "line_len == 10", else, ==12
				if line_len == 12:

					if type_p == True: #True = full;False = atoms
						data2.write(line)
					elif type_p == False:
						data2.write(str(line_ss[0])+'\t'+str(line_ss[2])+'\t'+
									str(line_ss[4])+'\t'+str(line_ss[5])+'\t'+
									str(line_ss[6])+'\n')
		return print('DataProcess done!')

	def Position(self,position_data,number_atom=True):
		pos = np.loadtxt(self.filename2,skiprows=15)
		# print(pos)
		pos_sort = pos[np.argsort(pos[:,0])]
		if number_atom ==True:
			np.savetxt(position_data,pos_sort[:,0:],'%d %d %f %f %f')
		else:
			np.savetxt(position_data,pos[:,1:],'%d %f %f %f')
		return

# ------Main Program--------#
# True = full;False = atoms

# type_p=True
type_p=False
# if need to save number of atoms, it is true
number_atom=True

ADLD = LAMMPSData()
if type_p==True:
	ADLD.ToFull('data_from_msi2lmp.data','Full.data',type_p)
else:
	ADLD.ToFull('data_from_msi2lmp.data','Atoms.data',type_p)
ADLD.Position('position.data',number_atom)
