#1 从获得的指定频率的波矢读取波矢，
#2 从位置信息文件读取位置信息
import numpy as np 
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=100000000)

def eigen_vector(filename1,filename2,filename3,number_atom=576):
	print('Waiting......!')

	with open(filename2)as position, \
	open(filename1)as eigenvector, \
	open(filename3,'w')as for_eigenvector:
		for_eigenvector.write('         ')
		for_eigenvector.write(str(number_atom))
		for_eigenvector.write('\n')
		for_eigenvector.write(' Mo S Se\n')
		# print(position.read())
		position_info = []
		for index, line in enumerate(position,1):
			line_position = line.strip().split()
			len_line = len(line_position)
			# print(len_line)
			if len_line==12:
				if line_position[2]=='1':
					position_info.append('S')
				elif line_position[2]=='2':
					position_info.append('Mo')
				elif line_position[2]=='3':
					position_info.append('Se')
				position_info.append(line_position[4])
				position_info.append(line_position[5])
				position_info.append(line_position[6])

		eigenvector_info = []
		for index, line in enumerate(eigenvector,1):
			if index>25*number_atom and index<=26*number_atom:
				line_eigenvector = line.strip().split()
				# print(line_eigenvector[0])
				eigenvector_info.append(line_eigenvector[1])
				eigenvector_info.append(line_eigenvector[3])
				eigenvector_info.append(line_eigenvector[5])

		position_array = np.array(position_info).reshape(number_atom,4)
		eigenvector_array = np.array(eigenvector_info).reshape(number_atom,3)
		eigenvector_ovito = np.hstack((position_array,eigenvector_array))

		##writedata
		#because of having str in matrix
		for i in range(number_atom):
			for j in range(7):
				for_eigenvector.write(str(eigenvector_ovito[i][j])+'      ')
			for_eigenvector.write('\n')

	return print(position_array.shape),print(eigenvector_array.shape),print(eigenvector_ovito.shape)

eigen_vector('eigenvector_4.1_4.5THz_MoS2-MoSe2','25_4x8_nanodot2period.data',\
	'eigenvector_4.454415THz_MoS2-MoSe2_25_4x8.dat',number_atom=384)
print('Done!')



