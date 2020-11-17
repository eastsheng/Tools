#Process the data from msi2lmp for lammps full
def DataProcess(filename1,filename2,number_of_atom_type=2):
	with open(filename1,'r')as data1,open(filename2,'w')as data2:
		for index, line in enumerate(data1,1):
			line_ss = line.strip().split()
			line_len = len(line_ss)
			# print(line)
			
			if index == 1:#header
				data2.write(line)

			if line_len == 2 and line_ss[1]=='atoms':#number atoms
				# print(line)
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
				data2.write(line)

	return print('DataProcess done!')

DataProcess('data_from_msi2lmp.data','Full.data')