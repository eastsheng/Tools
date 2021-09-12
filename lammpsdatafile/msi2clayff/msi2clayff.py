# rewrite the lammps data to fit the clayff from the msi2lmp.exe 
# e.g. this example, rewriting the hydroxyl SiO2 data

def readata(msi_data,clayff_data):
	with open(msi_data,'r') as msi:
		for index, line in enumerate(msi,1):
			if "Masses" in line:
				# print(index)
				Masses_index = index
			if "Pair Coeffs" in line:
				# print(index)
				Pair_coeffs_index = index
			if "Bond Coeffs" in line:
				# print(index)
				Bond_coeffs_index = index
			if "Angle Coeffs" in line:
				Angle_coeffs_index = index
			if "Atoms" in line:
				Atoms_index = index
			if "Bonds" in line:
				Bonds_index = index
			if "Angles" in line:
				Angles_index = index

	with open(msi_data,'r') as msi,open(clayff_data,'w') as clay:
		count = 0
		for index, line in enumerate(msi,1):					
			if index<Angle_coeffs_index:

				if index>Bond_coeffs_index and index<Angle_coeffs_index:

					if "oh-ho" in line:
						# print(line[3],type(line[3]))
						bond_type = line[3]
						line = "\n   1   553.9350     1.0000 # oh-ho\n\n"
						clay.write(line)

					else:
						pass
				else:

					clay.write(line)

			if index>=Atoms_index and index<=Bonds_index+1:
				clay.write(line)

			if index>Bonds_index and index<Angles_index and line!="\n":
				line = line.strip().split()

				if bond_type == line[1]:
					count = count + 1
					line[0] = str(count)
					line[1] = "1"
					# print(line)
					line = " ".join(line)
					clay.write(line+"\n")
		print(count,"bonds","\n0  angles", "\n0  dihedrals", "\n0  impropers\n")
		print("1  bond types","\n0  angle types", "\n0  dihedral types", "\n0  impropers")

	return 




if __name__ == '__main__':
	print("Modify your head info by hand:")
	# inital lammpsdata obtained from msi2lmp.exe tool
	msi_data = "quartz_alpha.data"
	clayff_data = "quartz_alpha_clayff.data"

	readata(msi_data,clayff_data)