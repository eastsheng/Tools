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
					min2.write('      ')
					min2.write(min_1[0])
					min2.write('      ')
					min2.write(min_1[1])					
					min2.write('  1  ')
					min2.write(min_1[3])
					min2.write('     ')					
					min2.write(min_1[4])
					min2.write('     ')				
					min2.write(min_1[5])
					min2.write('   ')
					min2.write(min_1[6])
					min2.write('   ')
					min2.write(min_1[7])
					min2.write('   ')					
					min2.write(min_1[8])
					min2.write('   ')					
					min2.write(min_1[9])
					min2.write(' ')
					min2.write(min_1[10])
					min2.write(' ')
					min2.write(min_1[11])				
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





