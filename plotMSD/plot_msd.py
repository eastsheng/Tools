# plot msd calculated by MD
import numpy as np
import matplotlib.pyplot as plt
def MSD(msdfile):
	msd = np.loadtxt(msdfile)
	len_msd = len(msd)
	# print(len_msd)
	msd = msd.reshape(int(len_msd/5),10)
	# print(msd)
	fs2ps = 5e-3
	# x1,y1 = msd[:,0]*fs2ps,msd[:,3]
	# x2,y2 = msd[:,0]*fs2ps,msd[:,5]
	# x3,y3 = msd[:,0]*fs2ps,msd[:,7]
	x4,y4 = msd[:,0]*fs2ps,msd[:,9]
	# plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
	# plt.show()
	return x4,y4

# ---main program--- #
if __name__ == '__main__':

	xa,ya=MSD('cation.msd')
	xb,yb=MSD('anion.msd')

	plt.rc('font', family='Times New Roman', size=16)
	plt.figure(figsize=(8,6))
	plt.plot(xa,ya,'r',label='cation')
	plt.plot(xb,yb,'b',label='anion')
	plt.legend()
	plt.xlabel('Time (ps)',size=20)
	plt.ylabel('MSD',size=20)
	plt.show()
