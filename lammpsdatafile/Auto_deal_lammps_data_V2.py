#Process the data from msi2lmp for lammps full or atoms
import numpy as np

class LAMMPSData(object):
	def ToFull(self,filename1,filename2,type_p):
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

					data2.write('\n')
					data2.write(line)
					data2.write('\n')

				if line_len == 12:

					if type_p == True: #True = full;False = atoms
						data2.write(line)
					elif type_p == False:
						data2.write(str(line_ss[0])+'\t'+str(line_ss[2])+'\t'+
									str(line_ss[4])+'\t'+str(line_ss[5])+'\t'+
									str(line_ss[6])+'\n')
		return print('DataProcess done!')

# ------Main Program--------#
# True = full;False = atoms

type_p=True
# type_p=False

ADLD = LAMMPSData()
if type_p==True:
	ADLD.ToFull('data_from_msi2lmp.data','Full.data',type_p)
else:
	ADLD.ToFull('data_from_msi2lmp.data','Atoms.data',type_p)
