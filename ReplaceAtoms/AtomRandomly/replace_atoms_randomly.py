#replace S atoms randomly in TMDs
import numpy as np
import random as rd
'''READ ratio of Se atoms from datafile or 
given directly'''
def read_ratio(datafilename,tot_atoms_number):
	global ratio
	global count	
	atoms=[]
	with open(datafilename,'r') as data:
		for index, line in enumerate(data,1):
			line = line.strip().split()				
			# print(data)
			len_line = len(line)
			# print(len_line)
			if len_line == 12:
				atoms.append(line)
	# print(atoms)
	Atoms = np.array(atoms)
	# print(Atoms.shape)
	count = 0
	for i in range(tot_atoms_number):

		if Atoms[i,2]=='3':#find Se atoms
			
			count = count+1 #count
	ratio = count/tot_atoms_number
	print('Number of Se atoms = ',count,'\nRatio = ',ratio,'\n')
	return  count, ratio

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



number_layers=200
size_flux_direction=54.02#nm
number_fixed = 2
number_bath = 2
size_everylayer=size_flux_direction/number_layers
size_fix_bath =  (number_fixed+number_bath)*size_everylayer*10

'''find the atoms that need to be replaced '''
def need_replace_list(pristinedata,replacelist,count):
	global Se_atoms
	read_cutoff(pristinedata)
	with open(pristinedata,'r')as pdata:
		S_atoms=[]
		for index, line in enumerate(pdata,1):
			line=line.strip().split()
			if index>cutoff+1:
				# print(line)
				#if it is S atom
				if line[2] == '1' and \
				float(line[4])>size_fix_bath and \
				float(line[4])<size_flux_direction*10-size_fix_bath:
					# print(line[0])
					S_atoms.append(line[0])
		print('除去固定层和热浴层后，一共有',len(S_atoms),'个S原子。')
		
		Se_atoms = []
		for i in range(count):
			random_atom = rd.choice(S_atoms)
			Se_atoms.append(random_atom)
		print('从中随机选取了',len(Se_atoms),'个被替换。')
	
	with open(replacelist,'w')as list_atoms:

		list_atoms.write('\n'.join(Se_atoms))

	return Se_atoms	


def write_random(pristinedata,write_data,count):
	read_cutoff(pristinedata)
	with open(pristinedata,'r')as pdata, open(write_data,'a')as wdata:
		for index, line in enumerate(pdata,1):
			line=line.strip().split()
			if index>cutoff+1:
				# print(line[0])
				if line[0] in Se_atoms:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    3      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
				else:
					wdata.write('      '+line[0]+'      '\
						+line[1]+'    '+line[2]+'      '+line[3]+'     '\
						+line[4]+'     '+line[5]+'     '\
						+line[6]+'   '+line[7]+'   '+line[8]+'   '\
						+line[9]+'   '+'\n')
	return  print('write random data Done!')

'''
read the ratio of periodic Se atoms from datafile
read_ratio(datafile,number of total atoms)
'''
read_ratio('20_5x8_MoS2-S209.data',9600)

'''
write the info of data header from datafile to random data
write_info(datafile,random data)
'''
write_info('20_5x8_MoS2-S209.data','MoS2_random_Se209.data')

'''
find the atoms of need to be replaced
need_replace_list(pristinedata,replaced number list,cout)
'''
need_replace_list('MoS2.data','Se_atoms.txt',count)

'''
write the rest of random data 
write_random(pristinedata,random data,cout)
'''
write_random('MoS2.data','MoS2_random_Se209.data',count)

print('All Done!\n')