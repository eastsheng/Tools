# select atoms from lammpsdata for calculating dos
import numpy as np
import re
import random
def readsize(filename):
    with open(filename,'r') as f:
        for i, line in enumerate(f,1):
            # print(line)          
            if 'xlo xhi' in line:              
                x = re.findall('(.*?) xlo xhi', line)[0].split(' ')
                x1 = float(x[0])
                x2 = float(x[1])
                # print(x1,x2)
                dx = x2-x1
    return x1,x2,dx


# lammps data
filename = './nvt.dat'
x1,x2,dx = readsize(filename)
# read position
data = np.loadtxt(filename,skiprows=15)
# print(data[:,0])
atom_id = data[:,0]
position_x = data[:,2]
position_y = data[:,3]
position_z = data[:,4]
layer_number = 100

scale = dx/layer_number

xmin = x1+6*scale
xmax = x2-6*scale

# the list doesn't include the heat and cold source regions
list_id = []

for i in range(len(position_x)):
    if position_x[i] >= xmin and position_x[i] <= xmax:
        list_id.append(atom_id[i])
# print(list_id)
print(len(list_id))

# select 32 atoms from the "list_id" 
select_list = random.sample(list_id,32)
select_list = np.array(select_list).reshape(1,32)
print(select_list)
np.savetxt('random_atoms.txt',select_list,"%d")
