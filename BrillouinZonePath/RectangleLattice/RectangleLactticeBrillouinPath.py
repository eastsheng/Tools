# Two Dimensional Rectangle Brillouin zone

import numpy as np

def RBrillouinPath(a1,a2):
	if a1>=a2:
		beta = a1/a2 #a1>=a2
		b1 = 0.5 # unit = 2pi/a
		b2 = 0.5*beta
	else:
		beta = a2/a1
		b1 = 0.5*beta # unit = 2pi/a
		b2 = 0.5
	print('Gamma-X: (0.0, 0.0, 0.0) --> ('+str(b1)+', 0.0'+', 0.0'+')')
	print('Gamma-M: (0.0, 0.0, 0.0) --> ('+str(b1)+', '+str(b2)+', 0.0'+')')
	return

a1 = 27.010
a2 = 24.952


RBrillouinPath(a1,a2)



