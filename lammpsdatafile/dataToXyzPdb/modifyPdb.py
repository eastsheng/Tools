# modify pdb file, add atoms types obtained from xyz file
import numpy as np
# np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

#read atom type from xyz file
def readAtomtype(xyz):
	with open(xyz,'r') as x:
		atom_style_list = []
		for index, line in enumerate(x,1):
			line_ss = line.strip().split()
			l_line = len(line_ss)
			if index>2:
				# print(line_ss)
				atom_style_list.append(line_ss[5])
	# l_list = len(atom_style_list)
	# atom_style_list = np.array(atom_style_list).reshape(l_list,1)
	# print(atom_style_list.shape)

	return atom_style_list

def RewritePdb(MS_pdb,MS_pdb_new,atom_style_list):
	with open(MS_pdb) as pdb, open(MS_pdb_new,'w') as pdb_new:
		for index, line in enumerate(pdb,1):
			line_ss = line.strip().split()
			# print(line_ss)
			l_line = len(line_ss)
			# print(l_line)
			if index<=2 or 'TER'in line_ss:
				pdb_new.write(line)
			elif l_line==11:
				# print(line)
				# print(line[77:81])
				line_new = line[:70]#+atom_style_list[index-2,0]
				line_new = line_new+atom_style_list[index-3]
				pdb_new.write(line_new+'\n')

	return

# ---main program--- #
if __name__ == '__main__':
	print("\n------Start!------\n")
	# your xyz file from "dataToxyz.py" tool
	xyz = "aaa13.xyz"
	# your pdb from MS based on your xyz
	MS_pdb = "aaa13.pdb"
	# modified pdbfile
	MS_pdb_new = "aaa13_new.pdb"


	atom_style_list = readAtomtype(xyz)
	# print(atom_style_list,len(atom_style_list))


	RewritePdb(MS_pdb,MS_pdb_new,atom_style_list)

	print("\n------Done!------\n")