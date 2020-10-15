import numpy as np
import matplotlib.pyplot as plt 
# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)

class SED(object):

	def read(self,result_data):
		self.sed_a = []
		self.sed_wav = []
		self.sed_fre = []
		self.sed_array=[]

		self.sed_a = np.loadtxt(result_data)
		self.sed_wav = np.unique(self.sed_a[:,0])
		self.sed_fre = np.unique(self.sed_a[:,1])
		lf = len(self.sed_fre)
		self.sed_fre = self.sed_fre.reshape(lf,1)
		lsed = int(len(self.sed_a)/lf)
		self.sed_sed = self.sed_a[:,2].reshape((lf,lsed))
		self.sed_array = np.hstack((self.sed_fre,self.sed_sed))
		print(self.sed_a.shape)
		print(self.sed_fre.shape)		
		print(self.sed_sed.shape)
		print(self.sed_array.shape)

		return

	def SaveSED(self,saveSEDfile,saveMEANfile):
		self.sed_mean = []
		sed_mean = np.mean(self.sed_sed,axis=1)
		sed_mean = sed_mean.reshape(len(sed_mean),1)
		# print(self.sed_sed.shape,sed_mean.shape)
		self.sed_mean = np.hstack((self.sed_fre,sed_mean))

		np.savetxt(saveSEDfile,self.sed_array,delimiter = ' ')
		np.savetxt(saveMEANfile,self.sed_mean,delimiter = ' ')

		return

	def PlotSED(self,ffile,rx,ry,savef=True,savedpi=300):
		self.figsx = 6
		self.figsy = 10
		x = self.sed_wav
		# print(x)
		y = self.sed_fre
		x,y = np.meshgrid(x,y)
		z = self.sed_sed
		z = np.log10(z/100)#log of sed
		normalied_zmax = np.max(z)
		print(normalied_zmax)		
		z = z/normalied_zmax#normalied

		plt.rc('font', family='Times New Roman', size=20)
		fig, ax = plt.subplots(figsize=(self.figsx, self.figsy))
		fig.subplots_adjust(bottom=0.1,left=0.2)
		plt.pcolormesh(x,y,z,cmap='jet',shading='gouraud')#rainbow  gouraud  
		#--------colorbar
		cb=plt.colorbar(shrink=0.8)#,fraction=.1)
		cb.set_label('Normalied log of spectral energy density',size=16)	
		cb.ax.tick_params(labelsize=16)#,labelright=False)	
		ax.set_xlabel('Wave vector',fontsize=32,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=32)		
		plt.xlim(rx)
		plt.ylim(ry)	
		if savef == True:
			plt.savefig(ffile,dpi=savedpi)			
		plt.show()
		plt.close()
		return

	def PlotMeanSED(self,):

		plt.rc('font', family='Times New Roman', size=20)
		plt.plot(self.sed_mean[:,0],self.sed_mean[:,1])
		plt.show()
		return

# ----------MAIN PROGRAM---------- #
savef = True
savedpi = 300

# plot range

rx = [0,1]
ry = [0,50]

sed = SED()
sed.read('result.sed_graphene80')
# sed.read('result.sed')

sed.SaveSED('sed_graphene80','sed_mean_frequency.dat_graphene80')
sed.PlotSED('sed.png',rx,ry,savef,savedpi)
sed.PlotMeanSED()