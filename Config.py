class conf(object):
	def __init__(self):
		self.h = 8 			#Number of attention layers
		self.N = 6			#Number of stacks
		self.dmodel = 512	#Number of feature
		self.dk = int(self.dmodel/self.h)
		self.dv = int(self.dmodel/self.h)
		self.dff = self.dk*self.h


		