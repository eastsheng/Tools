# read element id of molecules from lammpsdata for grouping
# Grouping for LAMMPS input file
import numpy as np
def readinfo(lammps_data):
	with open(lammps_data,'r') as data:
		for index, line in enumerate(data,1):
			if "Masses" in line:
				# print(index)
				Masses_index = index
			if "Atoms" in line:
				Atoms_index = index

	return Masses_index, Atoms_index


def readID(lammps_data):
	Atom_id = []
	Atom_type = []
	with open(lammps_data,'r') as data:
		for index, line in enumerate(data,1):
			if index>Masses_index and index<Atoms_index and line!="\n":
				line = line.strip().split()
				Atom_id.append(line[0])
				Atom_type.append(line[3]) 
		# print(Atom_id)
		# print(Atom_type)
		Atom_id_n = np.array(Atom_id).reshape(-1,1)
		Atom_type_n = np.array(Atom_type).reshape(-1,1)
		# print(Atom_id_n.shape,Atom_type_n.shape)
		ID_TYPE = np.hstack((Atom_id_n,Atom_type_n))
		# print(ID_TYPE)


	return ID_TYPE

def outputID(ID_TYPE,start,end):
	# print(ID_TYPE)
	# print(type(ID_TYPE))
	output = ID_TYPE[start-1:end,:]
	# print(output)
	C = []
	H = []
	O = []
	N = []
	S = []
	for i in range(end-start+1):
		if "C" in output[i,1][0]:
			# print(output[i,:])
			C.append(output[i,:])
		if "H" in output[i,1][0]:
			# print(output[i,:])
			H.append(output[i,:])
		if "O" in output[i,1][0]:
			# print(output[i,:])
			O.append(output[i,:])
		if "N" in output[i,1][0]:
			# print(output[i,:])
			N.append(output[i,:])
		if "S" in output[i,1][0]:
			# print(output[i,:])
			S.append(output[i,:])
	print("C"+str(len(C)),"H"+str(len(H)),"O"+str(len(O)),
		  "N"+str(len(N)),"S"+str(len(S))+"\n")
	C = np.array(C)
	H = np.array(H)
	O = np.array(O)
	N = np.array(N)
	S = np.array(S)
	
	
	return C,H,O,N,S

# ---------MAIN PROGRAM----------

if __name__ == '__main__':
	lammps_data = "system.data"
	Masses_index, Atoms_index = readinfo(lammps_data)
	# print(Masses_index,Atoms_index)
	ID_TYPE = readID(lammps_data)

	C1,H1,O1,N1,S1 = outputID(ID_TYPE,1,83)
	C2,H2,O2,N2,S2 = outputID(ID_TYPE,84,117)
	C3,H3,O3,N3,S3 = outputID(ID_TYPE,118,170)
	C4,H4,O4,N4,S4 = outputID(ID_TYPE,171,235)
	# print(C1)
	C_list = [C1, C2, C3, C4]
	H_list = [H1, H2, H3, H4]
	O_list = [O1, O2, O3, O4]
	N_list = [N1, N2, N3, N4]
	S_list = [S1, S2, S3, S4]

	with open("id.txt","w") as ID:
		for i in range(0,4):
			np.savetxt(ID,C_list[i].T,'%s',header='第'+str(i+1)+'个分子中C H O N S的原子ID')
			np.savetxt(ID,H_list[i].T,'%s')
			np.savetxt(ID,O_list[i].T,'%s')
			np.savetxt(ID,N_list[i].T,'%s')
			np.savetxt(ID,S_list[i].T,'%s')




