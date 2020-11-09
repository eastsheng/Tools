## Replace periodic Se-nanodot mass with gradient mass
## need to modify the info of data header, such as, 'atoms types','Masses'.

'''read the cutting line of data info and atoms position info from datafile'''
def read_cutoff(datafilename):
	with open(datafilename,'r')as pdata:
		global cutoff
		for index, line in enumerate(pdata,1):
			# print(type(line))

			if 'Atoms' in line:
				# print(index)
				cutoff = index
	return cutoff

'''for writing the info of data header'''
def write_info(datafilename,write_data):
	read_cutoff(datafilename)
	with open(datafilename,'r')as pdata, open(write_data,'w')as wdata:
		for index, line in enumerate(pdata,1):
			if index<=cutoff+1:
				wdata.write(line)
	return print('Write info Done!\n')

#-------The size of system is read from datafilename in MD simulation-------#
def Size(datafilename):
	'''Area of out of plane is obtained from NPT data.'''
	global system_size_x
	with open(datafilename,'r')as data:
		for line in data:
			line = line.strip().split()
			length_line = len(line)
			# print(length_line)
			if length_line==4 and line[2] in ['xlo','ylo','zlo']:
				# print(line)
				if line[2]=='xlo':
					xhi = float(line[1])
					xlo = float(line[0])
					system_size_x = (xhi-xlo)#/10#nm
				# elif line[2]=='ylo':
				# 	yhi = float(line[1])
				# 	ylo = float(line[0])					
				# 	system_size_y = (yhi-ylo)#/10#nm

	print('x =',system_size_x,'A')

	return	 system_size_x

def Write_GradientMass(pristinedata,write_data,chunknumber=4):

	gradient1 = system_size_x*((chunknumber-3)/chunknumber)
	gradient2 = system_size_x*((chunknumber-2)/chunknumber)
	gradient3 = system_size_x*((chunknumber-1)/chunknumber)
	gradient4 = system_size_x*((chunknumber-0)/chunknumber)

	read_cutoff(pristinedata)
	with open(pristinedata,'r')as pdata, open(write_data,'a')as wdata:
		for index, line in enumerate(pdata,1):
			line=line.strip().split()
			if index>cutoff+1:
				#if atom type is Se atom 
				if line[2] == '3' and float(line[4])<gradient1:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    '+line[2]+'      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
				elif line[2] == '3' and float(line[4])>=gradient1 and float(line[4])<gradient2:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    4      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
				elif line[2] == '3' and float(line[4])>=gradient2 and float(line[4])<gradient3:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    5      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
				elif line[2] == '3' and float(line[4])>=gradient3 and float(line[4])<gradient4:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    6      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
				else:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    '+line[2]+'      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')					
	return

Size('20_5x8_MoS2_Se209.data')
write_info('20_5x8_MoS2_Se209.data','20_5x8_MoS2_Se_GradientMass.data')
Write_GradientMass('20_5x8_MoS2_Se209.data','20_5x8_MoS2_Se_GradientMass.data',chunknumber=4)

