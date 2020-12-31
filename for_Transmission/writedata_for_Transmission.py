#write data for transmission

#import thermal_conductivity as TC

#-------The size of system are read from NPT_data in MD simulation-------#
def size(NPT_data,number_layers):
	global system_size_x
	global xlo,xhi
	with open(NPT_data,'r')as data:
		for line in data:
			line = line.strip().split()
			length_line = len(line)
			if length_line==4 and line[2] in ['xlo','ylo','zlo']:
				if line[2]=='xlo':
					xhi = float(line[1])
					xlo = float(line[0])
					system_size_x = (xhi-xlo)/10#nm
					print('Size of x direction of system =',system_size_x)
				elif line[2]=='ylo':
					yhi = float(line[1])
					ylo = float(line[0])					
					system_size_y = (yhi-ylo)/10#nm
					print('Size of y direction of system =',system_size_y)
	return print('size() done!')


#write data for calculating the Transmission
#default MoS2, if number_atom_type==3, it is MoS2-MoSe2 heterostructure
def write_dataforTransmission(filename1,filename2,number_atom_type=2):
	global xhi
	with open(filename1,'r')as former, open(filename2,'w')as latter:
		# data = former.read()
		# print(data)
		for index,line in enumerate(former,1):
			line_ss = line.strip().split()
			if index<=26:
				latter.write(line)	
			# print(line)
			size_line = len(line_ss)
			# print(size_line)
			if size_line==12:
				if float(line_ss[4])<=xhi/2:
					#If the x-coordinate less or equal than half of xhi, 
					#write pristine coordinate
					latter.write(line)
				elif float(line_ss[4])>xhi/2:
					#If it larger than half of xhi, 
					#judge the line[2](type of atom) whether == 1, is S atom
					if number_atom_type==3:
						if line_ss[2]=='1':
							# print('S')
							latter.write('   '+line_ss[0]+'   '+line_ss[1]+'   '\
								+str(4)+    '  '+line_ss[3]+'   '   +line_ss[4]+'     '+line_ss[5]+'     '\
								+line_ss[6]+'   '+line_ss[7]+'   '   +line_ss[8]+'   '+line_ss[9]+' '\
								+line_ss[10]+' '+line_ss[11])
							latter.write('\n')	
						#judge the line[2](type of atom) whether == 2, is Mo atom						
						elif line_ss[2]=='2':
							# print('Mo')
							latter.write('   '+line_ss[0]+'   '+line_ss[1]+'   '\
								+str(5)+    '  '+line_ss[3]+'   '   +line_ss[4]+'     '+line_ss[5]+'     '\
								+line_ss[6]+'   '+line_ss[7]+'   '   +line_ss[8]+'   '+line_ss[9]+' '\
								+line_ss[10]+' '+line_ss[11])
							latter.write('\n')						
						elif line_ss[2]=='3':
							# print('Se')
							latter.write('   '+line_ss[0]+'   '+line_ss[1]+'   '\
								+str(6)+    '  '+line_ss[3]+'   '   +line_ss[4]+'     '+line_ss[5]+'     '\
								+line_ss[6]+'   '+line_ss[7]+'   '   +line_ss[8]+'   '+line_ss[9]+' '\
								+line_ss[10]+' '+line_ss[11])
							latter.write('\n')	

					elif number_atom_type==2:
						if line_ss[2]=='1':
							# print('S')
							latter.write('   '+line_ss[0]+'   '+line_ss[1]+'   '\
								+str(3)+    '  '+line_ss[3]+'   '   +line_ss[4]+'     '+line_ss[5]+'     '\
								+line_ss[6]+'   '+line_ss[7]+'   '   +line_ss[8]+'   '+line_ss[9]+' '\
								+line_ss[10]+' '+line_ss[11])
							latter.write('\n')	
						#judge the line[2](type of atom) whether == 2, is Mo atom						
						elif line_ss[2]=='2':
							# print('Mo')
							latter.write('   '+line_ss[0]+'   '+line_ss[1]+'   '\
								+str(4)+    '  '+line_ss[3]+'   '   +line_ss[4]+'     '+line_ss[5]+'     '\
								+line_ss[6]+'   '+line_ss[7]+'   '   +line_ss[8]+'   '+line_ss[9]+' '\
								+line_ss[10]+' '+line_ss[11])
							latter.write('\n')	
	
	return print('write_dataforTransmission() done!')



#Calculating DeltaT for Transmission
def DeltaT_calculate():
	DeltaT = abs(Temperature_gradient*system_size_x)
	print('DeltaT=',round(DeltaT,4),'K')
	return DeltaT,print('DeltaT_calculate() done!')


size('MoS2_Defect25.data',200)

write_dataforTransmission('MoS2_Defect25.data',\
	'MoS2_Defect25_for_transmission.data',number_atom_type=3)

print('*******************')
print('****   Done!   ****')
print('****   Done!   ****')
print('*******************')