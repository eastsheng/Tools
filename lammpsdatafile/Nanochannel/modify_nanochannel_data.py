# delete the data beyond the nanochannel
import numpy as np
import os
import time

t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

class ModifyData(object):
	"""docstring for ModifyData"""
	def __init__(self, datafile,Lrange):
		super(ModifyData, self).__init__()
		self.datafile = datafile
		self.L0 = Lrange[0]
		self.L1 = Lrange[1]

	def read_index(self):
		with open(self.datafile,"r") as f:
			for index, line in enumerate(f,1):
				if "atoms" in line:
					self.atom_number = int(line.split()[0])
				if "Atoms # " in line:
					self.data_full_index = index+1

				if "Velocities" in line:
					self.Velocities_index = index+1

				if "bonds" in line:
					self.bonds_number = int(line.split()[0])
				if "Bonds" in line:
					self.Bonds_index = index+1
				if "angles" in line:
					self.angles_number = int(line.split()[0])
				if "Angles" in line:
					self.Angles_index = index+1
				if "dihedrals" in line:
					self.dihedrals_number = int(line.split()[0])
				if "Dihedrals" in line:
					self.Dihedrals_index = index+1
		return

	def modify_data_full(self,direction="x"):
		data_full = np.loadtxt(self.datafile,skiprows=self.data_full_index,max_rows=self.atom_number)
		m,n = data_full.shape
		data_full_sort = data_full[np.argsort(data_full[:,0])]
		del_id_list = []
		del_mol_list = []
		save_data_full = []
		for i in range(m):
			x,y,z = data_full_sort[i,4],data_full_sort[i,5],data_full_sort[i,6]
			if direction == "x":
				d = x
			elif direction == "y":
				d = y
			elif direction == "z":
				d = z
			if float(d)<self.L0 or float(d)>self.L1:
				del_mol_list.append(int(data_full_sort[i,1]))
		# print(del_id_list)
		# del_mol_list = np.unique(np.array(del_mol_list)).tolist()
		for i in range(m):
			if int(data_full_sort[i,1]) not in del_mol_list:	
				del_id_list.append(int(data_full_sort[i,0]))
				save_data_full.append(data_full_sort[i,:].tolist())
		save_data_full = np.array(save_data_full).reshape(-1,n)
		save_id_list = save_data_full[:,0]
		p, q = save_data_full.shape
		print("After delete, the atom number =",p)
		# for i in range(p):
		# 	save_data_full[i,0] = i+1
		np.savetxt("data_full.dat",save_data_full,fmt="%d %d %d %f %f %f %f %d %d %d")	
		# print(del_id_list,del_mol_list)
		return save_id_list

	def modify_Velocities(self,save_id_list):
		Velocities = np.loadtxt(self.datafile,skiprows=self.Velocities_index,max_rows=self.atom_number)
		m,n = Velocities.shape
		Velocities = Velocities[np.argsort(Velocities[:,0])]
		Velocities_list = []
		for i in range(m):
			if Velocities[i,0] in save_id_list:
				Velocities_list.append(Velocities[i,:])
		Velocities_array = np.array(Velocities_list).reshape(-1,4)
		p,q = Velocities_array.shape
		# for i in range(p):
		# 	Velocities_array[i,0] = i+1
		print("After delete, Velocities number =",p)
		np.savetxt("data_Velocities.dat",Velocities_array,fmt="%d %f %f %f")			
		return

	def modify_Bonds(self,save_id_list):
		Bonds = np.loadtxt(self.datafile,skiprows=self.Bonds_index,max_rows=self.bonds_number)
		m,n = Bonds.shape
		Bonds_list = []
		for i in range(m):
			if Bonds[i,2] in save_id_list and Bonds[i,3] in save_id_list:
				Bonds_list.append(Bonds[i,:])
		Bonds_array = np.array(Bonds_list).reshape(-1,4)
		p,q = Bonds_array.shape
		# for i in range(p):
		# 	Bonds_array[i,0] = i+1
		print("After delete, Bonds number =",p)	
		np.savetxt("data_Bonds.dat",Bonds_array,fmt="%d %d %d %d")	
		return

	def modify_Angles(self,save_id_list):
		Angles = np.loadtxt(self.datafile,skiprows=self.Angles_index,max_rows=self.angles_number)
		m,n = Angles.shape
		Angles_list = []
		for i in range(m):
			if Angles[i,2] in save_id_list and Angles[i,3] in save_id_list and Angles[i,4] in save_id_list:
				Angles_list.append(Angles[i,:])
		Angles_array = np.array(Angles_list).reshape(-1,5)
		p,q = Angles_array.shape
		# for i in range(p):
		# 	Angles_array[i,0] = i+1
		print("After delete, Angles number =",p)	
		np.savetxt("data_Angles.dat",Angles_array,fmt="%d %d %d %d %d")			
		return

	def modify_Dihedrals(self,save_id_list):
		Dihedrals = np.loadtxt(self.datafile,skiprows=self.Dihedrals_index,max_rows=self.dihedrals_number)
		m,n = Dihedrals.shape
		Dihedrals_list = []
		for i in range(m):
			if Dihedrals[i,2] in save_id_list and Dihedrals[i,3] in save_id_list\
			 and Dihedrals[i,4] in save_id_list and Dihedrals[i,4] in save_id_list:
				Dihedrals_list.append(Dihedrals[i,:])
		Dihedrals_array = np.array(Dihedrals_list).reshape(-1,6)
		p,q = Dihedrals_array.shape
		# for i in range(p):
		# 	Dihedrals_array[i,0] = i+1
		print("After delete, Dihedrals number =",p)
		np.savetxt("data_Dihedrals.dat",Dihedrals_array,fmt="%d %d %d %d %d %d")			
		return

	def rewrite_data(self):
		element_data = [
						"data_full.dat",
						"data_Velocities.dat",
						"data_Bonds.dat",
						"data_Angles.dat",
						"data_Dihedrals.dat",
		]
		label = ["Atoms  # full","Velocities","Bonds","Angles","Dihedrals"]
		with open("system_rewrite.data","w") as f, open(self.datafile,"r") as header:
			for _ in range(1,self.data_full_index-1):
				f.writelines(header.readline())

			for i in range(len(element_data)):
				f.write(label[i])
				f.write("\n\n")
				for line in open(element_data[i]):
					f.writelines(line)
				f.write("\n")	
		for i in range(len(element_data)):
			os.remove(element_data[i])
		return


if __name__ == '__main__':
	datafile = "1_push_nvt_300.data"

	direction = "x"
	Lrange = [212.86,413]

	md = ModifyData(datafile,Lrange)
	md.read_index()
	save_id_list = md.modify_data_full(direction) 
	md.modify_Velocities(save_id_list)
	md.modify_Bonds(save_id_list)
	md.modify_Angles(save_id_list) 
	md.modify_Dihedrals(save_id_list) 
	md.rewrite_data()


