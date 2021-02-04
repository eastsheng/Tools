# write lammps data from the modified pdb file
import numpy as np
import time
# np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

localtime = time.asctime(time.localtime(time.time()))

#read atom type from pdb file
def readAtomtype(pdbfile):
	with open(pdbfile,'r') as pdb:
		atom_style_list = []
		for index, line in enumerate(pdb,1):
			line_ss = line.strip().split()
			l_line = len(line_ss)
			if l_line>11:
				atom_style_list.append(line_ss[11])
			elif l_line>8 and l_line<=11:
				atom_style_list.append(line_ss[10])
	return atom_style_list

# write carfile obtained from MS
def rewritecar(MS_CAR,MS_CAR_new,atom_style_list):
	list_data = []
	with open(MS_CAR,'r') as car_before,\
	open(MS_CAR_new,'w') as car_new:
		for index, line in enumerate(car_before,1):
			if index<=4:
				car_new.write(line)
			# print(line)
			line_ss = line.strip().split()
			l_line = len(line_ss)
			if l_line==9:
				# print(line_ss)
				list_data.append(line_ss)

		car_array = np.array(list_data)
		len_data = len(car_array)
		atom_style_array = np.array(atom_style_list).reshape(len_data,1)
		# print(car_array)
		# print(atom_style_array)
		# print(car_array.shape,atom_style_array.shape)

		atom_type = np.unique(atom_style_array)
		print('Atoms type:\n',atom_type,'\n')
		atom_type = atom_type.reshape(len(atom_type),1)
		print('Atoms types number:',len(atom_type))
		m,n = car_array.shape
		x,y = atom_style_array.shape
		print('Atoms number',x)
		if m == x:
			for i in range(m):
				car_array[i,6] = atom_style_array[i,0]
		# print(car_array)
		for i in range(m):
			for j in range(n):
				car_new.write(car_array[i,j]+'\t')
			car_new.write('\n')
		car_new.write('end\nend')
	return 

# write carfile obtained from MS
def rewritemdf(MS_MDF,MS_MDF_new,atom_style_list):
	list_data=[]
	with open(MS_MDF,'r') as mdf_before,\
	open(MS_MDF_new,'w') as mdf_new:
		for index, line in enumerate(mdf_before,1):
			if index<=21:
				mdf_new.write(line)
			# print(line)
			line_ss = line.strip().split()
			l_line = len(line_ss)
			# print(l_line)
			if l_line>=12:
				list_data.append(line_ss)
				# print(len(list_data))
		
		print(list_data[0][2])
		l_list = len(list_data)
		l_atom_sl = len(atom_style_list)
		print(l_list,l_atom_sl)
		if l_list == l_atom_sl:
			for i in range(l_list):
				list_data[i][2] = atom_style_list[i]
				# print(list_data[i][2])
		# print(list_data)

		for i in range(l_list):
			s = str(list_data[i][:]).replace('[','').replace(']','')
			s = s.replace("'",'').replace(',','')
			mdf_new.write(s+'\n')
		mdf_new.write('\n#end')
	return


# ---main program--- #
if __name__ == '__main__':
	print("\n------Start!------\n")

	packmol_pdb = "ionmixture_Cu.pdb"

	MS_CAR = "ionmixture_Cu.car"
	MS_CAR_new = "ionmixture_Cu_new.car"

	MS_MDF = "ionmixture_Cu.mdf"
	MS_MDF_new = "ionmixture_Cu_new.mdf"

	# your pdb file from "packmol" tool
	atom_style_list = readAtomtype(packmol_pdb)
	# print(atom_style_list,len(atom_style_list))

	# rewritecar(MS_CAR,MS_CAR_new,atom_style_list)

	rewritemdf(MS_MDF,MS_MDF_new,atom_style_list)

	print("\n------Done!------\n")