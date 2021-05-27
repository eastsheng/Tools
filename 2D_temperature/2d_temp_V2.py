# rewrite the chunk position and temperature from 2d temperaure for ovito,xyz
# ref. S. Bazrafshan, A. Rajabpour/ International Journal of Heat and Mass Transfer 123 (2018) 534–543

import numpy as np

class TwoDTxyz(object):
	"""docstring for ClassName"""
		
	def rewrite_xyz(self,twod_tfile,ovito_xyz,size_x,size_y):
		fopen = np.loadtxt(twod_tfile,skiprows=4)
		chunk_number = len(fopen)
		self.chunk_number = chunk_number
		# print(fopen)
		c = "C "*chunk_number
		c = c.split()
		c = np.array(c).reshape(chunk_number,1)

		x = fopen[:,1:2]*size_x
		self.x = x
		y = fopen[:,2:3]*size_y
		z = np.zeros((chunk_number,1))
		t = fopen[:,4]
		cxyzt = np.c_[c,x,y,z,t]
		# print(cxyzt)
		print(cxyzt.shape)
		m,n = cxyzt.shape

		# wopen = np.savetxt(ovito_xyz,cxyzt,fmt="%s")
		wopen = open(ovito_xyz,'w')
		wopen.write(str(chunk_number)+'\nAtoms. Timestep: 2000\n')
		for i in range(m):
			for j in range(n):
				if j==n-1:
					wopen.write(cxyzt[i,j]+'\t\n')
				else:
					wopen.write(cxyzt[i,j]+'\t')
		wopen.close()

		return cxyzt

	def cell_xyz(self,ovito_cellxyz,cxyzt,period,out_pn):
		x = self.x
		x_max = max(x)
		x_min = min(x)
		length_x = float(x_max)-float(x_min)
		period_len = length_x/period
		m,n = cxyzt.shape

		print(length_x)
		copen = open(ovito_cellxyz,'w')
		copen.write(str(int(self.chunk_number/period))+'\nAtoms. Timestep: 2000\n')
		for i in range(m):
			for j in range(n):
				if x[i] >= x_min+ period_len*(out_pn-1) and x[i] < x_min+ period_len*(out_pn):
					print(x)
					if j==n-1:
						copen.write(cxyzt[i,j]+'\t\n')
					else:
						copen.write(cxyzt[i,j]+'\t')
		copen.close()		
		return


# ------MAIN PROGRAM------#

size_x = 546.834226427108 #angstrom
size_y = 50.7569489853392
# total period number
period = 10
# output period number xyz
out_pn = 2

twod_tfile = './1_temp_equ_300K.dat'
ovito_xyz = './1_temp_equ_300K.xyz'
ovito_cellxyz = './1_temp_equ_300K_'+str(out_pn)+'cell.xyz'

if __name__ == '__main__':
	twodt = TwoDTxyz()
	cxyzt = twodt.rewrite_xyz(twod_tfile,ovito_xyz,size_x,size_y)
	twodt.cell_xyz(ovito_cellxyz,cxyzt,period,out_pn)
