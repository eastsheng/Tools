# 批量处理文件名：把文件中的数字前面的0去掉
import os
import re
def ReName():
	ls = os.listdir()
	# print(ls,type(ls))
	len_ls = len(ls)
	harmls = []
	oldnumber = []
	# 从文件夹里读取所有文件名，并筛选
	for i in range(len_ls):
		if 'lammps' in ls[i].split('.') and 'cub' in ls[i].split('ic'):
			# print(ls[i])
			harmls.append(ls[i])
	len_harmls = len(harmls)
	# print(len_harmls)
	# 从筛选后的文件名中读取数字
	old_name = harmls
	# print(old_name)
	for i in range(len(old_name)):
		oldn = re.findall("cubic(.*?).lammps",old_name[i])[0]
		oldnumber.append(oldn)
	# print(oldnumber)

	for i in range(len(old_name)):
		os.rename('cubic'+oldnumber[i]+'.lammps','cubic'+str(int(oldnumber[i]))+'.lammps')
	return

ReName()
