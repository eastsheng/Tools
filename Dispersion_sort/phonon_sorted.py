def phonon_sort(filename1,filename2):

	k_point = 50#k_point数

	with open(filename1) as sort_before,open(filename2,'w') as p_sort_after:
		sort = sort_before.read().strip().split()
		# print(sort)
		sort = map(eval,sort)
		sort = list(sort)

		print('总元素数：',len(sort))

		row_number = int(len(sort)/k_point)#原本每一行数字的数量

		print('\n每一行元素数：',row_number,'其中前三个是K点\n')
		atom_number = int((row_number-3)/3)
		print('原子个数：',atom_number)

		for i in range(k_point):
			# print(i)
			for j in range(i*row_number,(i+1)*row_number):
				# print(sort[j])
				# print(j)
				sortly = round(sort[j],6)#保留6位有效数字
				sortly = str(sortly/33.36)#单位转换1THz=33.36cm-1
				p_sort_after.write(sortly)
				# p_sort_after.write(str(sortly))
				p_sort_after.write('        ')
			p_sort_after.write('\n')

		return 

phonon_sort('phonon_sorted.dat','p_sorted_20')