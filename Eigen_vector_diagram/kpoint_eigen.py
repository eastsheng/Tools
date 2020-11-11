# converting K-point to eigen vector(Normized)

class KpointVector(object):
	"""docstring for ClassName"""
	def __init__(self, kp_number):
		super(KpointVector, self).__init__()
		self.kp_number = kp_number

		return
	def KconvertV(self,kp):
		vec = kp/self.kp_number

		print("K point:",kp,"converted normalized vector:",vec)
		return

	def VconvertK(self,vec):
		kp = self.kp_number*vec
		print("Eigen Vector:",vec,"converted k point:",kp)
		

# k-point total number
kp_number = 50

# kpoint that needs to converted (<kp_number)
kp = 21
# eigen vector that needs to converted (0-1)
vec = 0.2

kpv = KpointVector(50)
kpv.KconvertV(kp)
kpv.VconvertK(vec)