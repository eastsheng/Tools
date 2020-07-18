## The parameter conversion between LAMMPS and GULP.
import numpy as np

def LammpsToGulp(epsilon,sigma,a,Lambda,gamma,costheta0,A_LAMMPS,B_LAMMPS,p,q,tol,gulpfilename):

	##SW2

	A_GULP = A_LAMMPS
	rho_SW2 = sigma
	B_GULP = round(B_LAMMPS*(rho_SW2**4),4)
	rmin = 0.000
	rmax = round(a*rho_SW2,4)
	print('\nSW2 for GULP:')
	print('A','rho','B','rmin','rmax')
	print(A_GULP,rho_SW2,B_GULP,rmin,rmax)

	## SW3
	K = Lambda
	theta0 = round(np.arccos(costheta0)*(180/np.pi),4)
	rho1_SW3 = round(rho_SW2*gamma,4)
	rho2_SW3 = round(rho_SW2*gamma,4)

	rmin12 = 0.00
	rmax12 = round(a*rho2_SW3,4)

	rmin13 = 0.00
	rmax13 = round(a*rho2_SW3,4)

	rmin23 = 0.00
	rmax23 =  round(a*rho2_SW3,4)##rmax23怎么获取?
	
	GPlist = [K,theta0,rho1_SW3,rho2_SW3,rmin12,rmax12,rmin13,rmax13,rmin23,rmax23]
	GParray = np.array(GPlist).reshape((1,10))
	# print(GParray)
	print('\nSW3 for GULP:')
	print('K','theta0','rho1','rho2','rmin12','rmax12','rmin13','rmax13','rmin23','rmax23')
	print(K,theta0,rho1_SW3,rho2_SW3,rmin12,rmax12,rmin13,rmax13,rmin23,rmax23)
	np.savetxt(gulpfilename,GParray,fmt='%.4f')
	return print('Done!\n')


##--------start--------##
LP = np.loadtxt('LammpsPotentialParam.txt')
# print(LP.shape)
epsilon = LP[0]
sigma = LP[1]
a = LP[2]
Lambda = LP[3]
gamma = LP[4]
costheta0 = LP[5]
A_LAMMPS = LP[6]
B_LAMMPS = LP[7]
p = LP[8]
q = LP[9]
tol = LP[10]

LammpsToGulp(epsilon,sigma,a,Lambda,gamma,costheta0,A_LAMMPS,B_LAMMPS,p,q,tol,'GulpPotentialParam.txt')


