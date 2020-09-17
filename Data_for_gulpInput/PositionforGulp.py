# FOR CARTESIAN POSITION OF GULP
class GulpGin(object):
	"""GULP cartesian position"""
	def Var(self,atom_type_1,atom_type_2,atom_type_3,only_position=True):
		self.atom_type_1 = atom_type_1
		self.atom_type_2 = atom_type_2
		self.atom_type_3 = atom_type_3
		# self.atom_type_4 = atom_type_4
		self.only_position = only_position
		return

	def Write_position_for_gulp(self,datafromlammps,dataforgulp):
		'''write position infomation from lammps data file 
		for gulp inputfile'''
		with open(datafromlammps) as min1,open(dataforgulp,'w') as min2:
			for index, line in enumerate(min1,1):
				# print(line)
				min_1 = line.strip().split()
				length_line = len(min_1)
				# print(length_line)
				if length_line==12:
					print(min_1)
					# min2.write(min_1[0])
					# min2.write('   ')
					if min_1[2] == str(1):
						min2.write(self.atom_type_1)
					elif min_1[2] == str(2):
						min2.write(self.atom_type_2)
					elif min_1[2] == str(3):
						min2.write(self.atom_type_3)

					min2.write('\t\t\tcore\t\t\t')
					min2.write(min_1[4]+'\t\t\t'+min_1[5]+'\t\t\t')				
					min2.write(min_1[6]+'\t\t\t')
					if only_position == True:
						min2.write('\n')
					else:					
						min2.write('0.0\t\t\t1.0\t\t\t0.0\t\t\t1 1 1\t\t\t#')				
						min2.write(min_1[0]+'\n')
					
		return print('Write position done!')

# Main Program
# Atom type symbols
atom_type_1 = 'C1'
atom_type_2 = 'C2'
atom_type_3 = 'N'
# only position?
only_position = False

gulp = GulpGin()	
gulp.Var(atom_type_1,atom_type_2,atom_type_3,only_position)
gulp.Write_position_for_gulp('FixGRA_0_C3N.dat','FixGRA_0_C3N.core')