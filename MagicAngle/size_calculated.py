import numpy as np

size = np.loadtxt('outplane_angle.txt')
a = size[:,1:]
x = 12/(size[:,1:]/10)
# print(x)

x = np.rint(x)

# print(x)

# print(x*a)

y = np.hstack((x*a/10,x))
print(y)
np.savetxt('xy.txt',y,'%f %f %d %d')
