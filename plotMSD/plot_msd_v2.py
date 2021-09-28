# plot msd calculated by MD
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def MSD(msdfile):
	msd = np.loadtxt(msdfile)
	len_msd = len(msd)
	# print(len_msd)
	msd = msd.reshape(int(len_msd/5),10)
	# print(msd)
	timestep = 2
	fs2ps = timestep*5e-3
	x1,y1 = msd[:,0]*fs2ps,msd[:,3]
	x2,y2 = msd[:,0]*fs2ps,msd[:,5]
	x3,y3 = msd[:,0]*fs2ps,msd[:,7]
	x4,y4 = msd[:,0]*fs2ps,msd[:,9]
	# plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
	# plt.show()
	return x4.reshape(-1, 1),y4.reshape(-1, 1)

# ---main program--- #
if __name__ == '__main__':

	xa,ya=MSD('msdSat.msd')
	print(xa.shape,ya.shape)
	xb,yb=MSD('msdAro.msd')
	xc,yc=MSD('msdRes.msd')
	xd,yd=MSD('msdAsp.msd')

	plt.rc('font', family='Times New Roman', size=16)
	plt.figure(figsize=(16,6))
	plt.subplot(121)
	plt.plot(xa,ya,'r',label='Sat')
	plt.plot(xb,yb,'b',label='Aro')
	plt.plot(xc,yc,'y',label='Res')
	plt.plot(xd,yd,'g',label='Asp')	
	plt.legend()
	plt.xlabel('Time (ps)',fontweight='bold',size=20)
	plt.ylabel('MSD($\mathregular{Å^2}$)',fontweight='bold',size=20)
	# plt.show()

	Aps2ms=1e-20*1e12
	msforplot = 1e12

	diffusion_a = LinearRegression(fit_intercept = False).fit(xa,ya).coef_[0, 0]/6*Aps2ms
	diffusion_b = LinearRegression(fit_intercept = False).fit(xb,yb).coef_[0, 0]/6*Aps2ms
	diffusion_c = LinearRegression(fit_intercept = False).fit(xc,yc).coef_[0, 0]/6*Aps2ms
	diffusion_d = LinearRegression(fit_intercept = False).fit(xd,yd).coef_[0, 0]/6*Aps2ms
	diffusion = np.array([diffusion_a,diffusion_b,diffusion_c,diffusion_d])*msforplot
	x_list = ["Sat","Aro","Res","Asp"]
	print(diffusion)
	plt.subplot(122)
	plt.xlabel('Heavy Oil',fontweight='bold',size=20)
	plt.ylabel('Diffusion coefficient($\mathregular{10^{-12}m^{2}s^{-1}}$)',fontweight='bold',size=20)	
	plt.bar(x_list[0],diffusion[0],color="r")
	plt.bar(x_list[1],diffusion[1],color="b")
	plt.bar(x_list[2],diffusion[2],color="g")
	plt.bar(x_list[3],diffusion[3],color="y")
	plt.show()


