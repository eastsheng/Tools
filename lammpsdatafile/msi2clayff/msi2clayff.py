# rewrite the lammps data to fit the clayff from the msi2lmp.exe 
# e.g. this example, rewriting the hydroxyl SiO2 data
# J. Phys. Chem. B, Vol. 108, No. 4, 2004 1259

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
			if "Dihedral Coeffs" in line:
				Dihedral_coeffs_index = index
			if "Atoms" in line:
				Atoms_index = index
			if "Bonds" in line:
				Bonds_index = index
			if "Angles" in line:
				Angles_index = index	
			if "Dihedrals" in line:
				Dihedrals_index = index	

	with open(msi_data,'r') as msi,open(clayff_data,'w') as clay:
		count_bond = 0
		count_angle = 0
		for index, line in enumerate(msi,1):
			if index <=	Bond_coeffs_index or index == Angle_coeffs_index:
				clay.write(line)			

			if index>Bond_coeffs_index and index<Angle_coeffs_index:

				if "oh-ho" in line:
					# print(line[3],type(line[3]))
					bond_type = line[3]
					line = "\n   1   554.1349     1.0000 # oh-ho\n\n"
					clay.write(line)

			if index>Angle_coeffs_index and index<Dihedral_coeffs_index:

				if "oh-sz-oz" in line:
					# print(line[3],type(line[3]))
					angle_type = line[3]
					line = "\n   1   30.0     109.47 # oh-sz-oz\n\n"
					clay.write(line)



			if index>=Atoms_index and index<=Bonds_index+1 or index==Angles_index or index==Angles_index+1 or index==Angles_index-1:
				clay.write(line)
			if index>Bonds_index and index<Angles_index and line!="\n":
				line = line.strip().split()
				if bond_type == line[1]:
					count_bond = count_bond + 1
					line[0] = str(count_bond)
					line[1] = "1"
					# print(line)
					line = " ".join(line)
					# print(line,type(line))
					clay.write(line+"\n")
			if index>int(Angles_index) and index<int(Dihedrals_index) and line!="\n":
				line = line.strip().split()
				if angle_type == line[1]:
					count_angle = count_angle + 1
					line[0] = str(count_angle)
					line[1] = "1"
					# print(line)
					line = " ".join(line)
					# print(line,type(line))
					clay.write(line+"\n")

		print(count_bond,"bonds")
		print(count_angle,"angles", "\n0  dihedrals", "\n0  impropers\n")
		print("1  bond types","\n1  angle types", "\n0  dihedral types", "\n0  impropers")

	return 




if __name__ == '__main__':
	print("Modify your head info by hand:")
	# inital lammpsdata obtained from msi2lmp.exe tool
	msi_data = "quartz_alpha_unitcell.data"
	clayff_data = "quartz_alpha_unitcell_clayff.data"

	readata(msi_data,clayff_data)