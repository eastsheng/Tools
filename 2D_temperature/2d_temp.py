# rewrite the chunk position and temperature from 2d temperaure for ovito,xyz
# ref. S. Bazrafshan, A. Rajabpour/ International Journal of Heat and Mass Transfer 123 (2018) 534–543

import numpy as np

def rewrite_xyz(twod_tfile,ovito_xyz,size_x,size_y):
	fopen = np.loadtxt(twod_tfile,skiprows=4)
	chunk_number = len(fopen)
	# print(fopen)
	c = "C "*chunk_number
	c = c.split()
	c = np.array(c).reshape(chunk_number,1)

	x = fopen[:,1:2]*size_x
	y = fopen[:,2:3]*size_y
	z = np.zeros((chunk_number,1))
	t = fopen[:,4]
	cxyzt = np.c_[c,x,y,z,t]
	# print(cxyzt)
	print(cxyzt.shape)
	m,n = cxyzt.shape

	# wopen = np.savetxt(ovito_xyz,cxyzt,fmt="%s")
	wopen = open(ovito_xyz,'w')
	wopen.write(str(chunk_number)+'\nAtoms. Timestep: 200\n')
	for i in range(m):
		for j in range(n):
			if j==n-1:
				wopen.write(cxyzt[i,j]+'\t\n')
			else:
				wopen.write(cxyzt[i,j]+'\t')
	wopen.close()

	return 

# ------MAIN PROGRAM------#

size_x = 546.834226427108 #angstrom
size_y = 50.7569489853392

twod_tfile = './pristine/1_temp_equ_300K.dat'
ovito_xyz = './pristine/1_temp_equ_300K.xyz'


if __name__ == '__main__':
	rewrite_xyz(twod_tfile,ovito_xyz,size_x,size_y)
