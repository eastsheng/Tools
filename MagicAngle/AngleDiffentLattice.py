#对于不同的晶格常数的转角，例如GRA/MoS2

import numpy as np

def Angle(n,m):
	if m==0 and n==0:
		print("\n注意：“跳过m和n同时为0的情况,并设其角度为0”\n")
		angle = 0.000
	else:
		x = (m**2+4*m*n+n**2)/(m**2+m*n+n**2)/2

		angle = np.arccos(x)*(180/np.pi)/2
		angle = round(angle,2)

	print(angle)
	return angle


def Number_of_Aotm(n1,m1,n2,m2):
	# Number_data=open('result.txt','a')
	NOA1 = 4*(m1**2+m1*n1+n1**2)
	NOA2 = 6*(m2**2+m2*n2+n2**2)
	NOA = NOA1+NOA2
	print(NOA1,NOA2,NOA)

	return NOA1,NOA2,NOA

##main program##
n1,m1,n2,m2 = [4,1,3,1]

angle_all = Angle(n1,m1)+Angle(n2,m2)
print(angle_all)
Number_of_Aotm(n1,m1,n2,m2)
# print(np.sqrt(3))





