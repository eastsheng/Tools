# 由于SiO2表面O原子带电荷，而内部不带电荷
# 因此，进行区分
# 修改羟基化的SiO2结构pdb文件(从MS导出)

def modify_O(pdb_in,pdb_out):
	with open(pdb_in,'r') as pdb_i, \
		 open(pdb_out,'w') as pdb_o:
		for index, line in enumerate(pdb_i,1):
			liness = line.strip().split()
			len_line = len(liness)
			# print(liness,len(liness))
			if len_line!=11:
				pdb_o.write(line)
			else:
				if liness[10] == "O":
					# 默认判断O原子在Z方向坐标，自己把握
					if float(liness[7])>16:
						# print(line[13])
						line_list = list(line)
						line_list[14] = "1"
						line_s = "".join(line_list)
						pdb_o.write(line_s)
					else:
						pdb_o.write(line)
				else:
					pdb_o.write(line)

					# print(line)

	return

# ---MAIN--- #
pdb_in = "quartz_alpha.pdb"
pdb_out = "quartz_alpha_out.pdb"
modify_O(pdb_in,pdb_out)