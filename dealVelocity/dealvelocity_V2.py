import numpy as np 
import matplotlib.pyplot as plt 

'''only have velocity of x, y and z direction in the velocity file, \
may include atomic id.'''
def velocity_a(filename1,filename2,Atom_ID=False):
	"""Processing atomic velocity files output by lammps,
	 that is, remove the periodic header of the velocity file"""
	with open(filename1,'r') as reader, open(filename2,'w') as writer:
		for index, line in enumerate(reader,1):
			# print(line)
			Line = line.strip().split()
			length_line = len(Line)
			# print(length_line)
			if Atom_ID == True:
				length_velocityline = 5
			else:
				length_velocityline = 3

			if length_line == length_velocityline:
				# writer.write(Line[0])
				# writer.write('   ')
				# writer.write(Line[1])
				# writer.write('   ')
				writer.write(Line[2])
				writer.write('   ')
				writer.write(Line[3])
				writer.write('   ')
				writer.write(Line[4])				
				writer.write('\n')

	return  print('velocity_a() done!')

def plotDOS(dos):
	data = np.loadtxt(dos)
	# print(data)
	x = data[:,0]
	y = data[:,1]
	plt.plot(x,y)
	plt.show()

	return  print('plotDOS() done!')


# velocity_a('DOS.velocity','DOS_nohead1.velocity',Atom_ID=True)
plotDOS('DOS.dos')