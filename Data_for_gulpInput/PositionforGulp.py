def Write_position_for_gulp(datafromlammps,dataforgulp,
	atom_type_1,atom_type_2,atom_type_3,only_position=True):
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
					min2.write(atom_type_1)
				elif min_1[2] == str(2):
					min2.write(atom_type_2)
				elif min_1[2] == str(3):
					min2.write(atom_type_3)
				min2.write('   core   ')
				min2.write(min_1[4]+'   '+min_1[5]+'   ')				
				min2.write(min_1[6]+'   ')
				if only_position == True:
					min2.write('\n')
				else:					
					min2.write('0.0   1.0   0.0   1 1 1   #')				
					min2.write(min_1[0]+'\n')
				
	return print('Write_position_for_gulp() done!')

# Main Program
# Atom type symbols
atom_type_1 = 'C1'
atom_type_2 = 'C2'
atom_type_3 = 'N'
# only position?
only_position = True

	
Write_position_for_gulp('FixGRA_0_C3N.dat','FixGRA_0_C3N.core',
	atom_type_1,atom_type_2,atom_type_3,only_position)