# Written on April 29, 2020 by eastsheng
#Tool 1
def writedata_a(filename1,filename2):
	'''This function is used to modify the atom type
	 of data exported from lammps, and change all atoms 
	 to one type of atom '''
	with open(filename1,'r') as min1\
	,open(filename2,'w') as min2:
		for index, line in enumerate(min1,1):
			if index < 25:
				min2.write(line)
			else:
				min_1 = line.strip().split()
				length_line = len(min_1)
				# print(length_line)
				if length_line==12:
					min2.write('      '+min_1[0] +'      '+min_1[1]+'  1  '+min_1[3])					
					min2.write('     ' +min_1[4] +'      '+min_1[5]+'   '  +min_1[6])					
					min2.write('   '   +min_1[7] +'   '   +min_1[8]+'     '+min_1[9])
					min2.write(' '     +min_1[10]+' '     +min_1[11])				
					min2.write('\n')
	return print('\nwritedata_a() done!\n')

#Tool 2
'''velocity of x, y and z direction in the velocity file,
may include atomic id.'''
def velocity_a(filename1,filename2,Atom_ID=False):
	"""Processing atomic velocity files output by lammps,
	 that is, remove the periodic header of the velocity file"""
	with open(filename1,'r') as reader, open(filename2,'w') as writer:
		for index, line in enumerate(reader,1):
			# print(line)
			Line = line.strip().split()
			length_line = len(Line)
			# print(length_line)
			''' if have atomic id'''
			if Atom_ID == True:
				length_velocityline = 4
			else:
				length_velocityline = 3

			if length_line == length_velocityline:
				writer.write(Line[0])
				writer.write('   ')
				writer.write(Line[1])
				writer.write('   ')
				writer.write(Line[2])
				writer.write('\n')

	return  print('velocity_a() done!')

#Tool 3

def eigen_vector(filename1,filename2,filename3,number_atom=576):
	''' write MoS2-MoSe2 data file for ovito, eigen_vector(
	eigenvectorfile from GULP, primitive cell file, data for ovitio, 
	atom number of primitive cell)'''
	print('Waiting......!')

	with open(filename2)as position, \
	open(filename1)as eigenvector, \
	open(filename3,'w')as for_eigenvector:
		for_eigenvector.write('         ')
		for_eigenvector.write(str(number_atom))
		for_eigenvector.write('\n')
		for_eigenvector.write(' Mo S Se\n')
		# print(position.read())
		for index, line in enumerate(position,1):
			line_position = line.strip().split()
			len_line = len(line_position)
			# print(len_line)
			if len_line==12:
				# print(line_position)
				# for_eigenvector.write(line_position[0])
				for_eigenvector.write('         ')
				if line_position[2]=='1':
					for_eigenvector.write('S')
					for_eigenvector.write('      ')
				elif line_position[2]=='2':
					for_eigenvector.write('Mo')
					for_eigenvector.write('      ')
				elif line_position[2]=='3':
					for_eigenvector.write('Se')
					for_eigenvector.write('      ')
				for_eigenvector.write(line_position[4]+'       ')
				for_eigenvector.write(line_position[5]+'       ')
				for_eigenvector.write(line_position[6]+'       \n')
				
		for index, line in enumerate(eigenvector,1):
			if index<=number_atom:
				line_eigenvector = line.strip().split()
				for_eigenvector.write(line_eigenvector[1])
				for_eigenvector.write('       ')
				for_eigenvector.write(line_eigenvector[3])
				for_eigenvector.write('       ')
				for_eigenvector.write(line_eigenvector[5])
				for_eigenvector.write('\n')
			elif number_atom<index<=2*number_atom:
				break
	return  print('eigen_vector() Done!')
# eigen_vector('eigenvector_4_MoS2','Mos2_4primitivecells.data','eigenvector_4.143906THz_4_MoS2_33_3x8.dat')

#Tool 4

def Write_position_for_gulp(datafromlammps,dataforgulp):
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

					min2.write('S')
				elif min_1[2]  == str(3):
					min2.write('Se')
				else:
					min2.write('Mo')
				min2.write('   core   ')
				min2.write(min_1[4]+'   '+min_1[5]+'   ')				
				min2.write(min_1[6]+'   ')
				min2.write('0.0   1.0   0.0   1 1 1   #')				
				min2.write(min_1[0]+'\n')
	return print('Write_position_for_gulp() done!')

