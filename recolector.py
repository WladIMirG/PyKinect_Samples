from pykinect import nui
import scipy.io as ScIO
import numpy as np

class NubePuntos(object):
	""""""
	nube = []
	x = []
	y = []
	z = []
	w = []
	def add_punto(self, fila):
		for punto in fila:
			self.x.append(punto.x)
			self.y.append(punto.y)
			self.z.append(punto.z)
			self.w.append(punto.w)
		self.nube.append(fila)

	def __iter__(self):
		return iter(self.nube)
	def iteritems(self):
		return self.nube.iteritems()
	def clear_nube(self):
		self.nube = []
def guardar1(Dato):
	"""Guarda los datos en un archivo *.m legible desde Octave y MATLAB"""
	ScIO.savemat('Nuevos_cursor.mat', mdict={'NewPos': Dato})

def guardar(Dato):
	"""Guarda los datos en un archivo *.m legible desde Octave y MATLAB"""
	ScIO.savemat('Nuevos_cursor.mat', mdict={'NewPos': Dato})
	np.save('Nuevos_cursor.mat', Dato)

class recolector(object):
	lim = 1.2
	nube = NubePuntos()
	depth = None
	def __init__(self):
		self.rlt = []
		self.x = np.array(range(320))/320.0
		self.y = np.array(range(240))/240.0
		#xx = np.array(range (0,320))/320.0
		#num = 0
		#for i in range(0,240): self.x = np.append(self.x, xx)
		#for i in self.x:
		#	if i < 319.0:
		#		self.y = np.append(self.y, num/240)
		#	elif i == 319.0:
		#		self.y = np.append(self.y, num/240)
		#		num += 1
	def recolectar(self):
		self.nube.clear_nube()
		if self.depth is None:
			print 'voy a retornar'
			return
		self.rlt = self.depth/2842.5
		fila = []
		depth = np.append(self.depth, [])
		depth = depth.astype(int)
		#print depth
		#depth = np.array(depth, np.uint)
		
		i = 0
		j = 0
		k = 0
		#print 'la longitud de z: ', z.size
		for K in depth:
			
			punto = nui.SkeletonEngine.depth_image_to_skeleton(self.x[j],
															   self.y[i],
															   K)
			if punto.z > 0 and punto.z < self.lim:
			#print 'Este es el limite actual: %f'%(float(lim))
				self.rlt[i, j, 0] = 1
				fila.append(punto)
				#print '<x: %f y: %f z:%f>'%(x[k],y[k],z[k])
			else:
				self.rlt[i, j, 0] = 0
			print i, j
			if i < 239:
				if j < 319:
					j += 1
				else:
					j = 0
					i += 1
			else:
				j = 0
				i = 0
			k += 1
		self.nube.add_punto(fila)

	def recolectar2(self):
		self.nube.clear_nube()
		if self.depth is None:
			print 'voy a retornar'
			return
		self.rlt = self.depth/2842.5
		for filas in range(0,240,1):
			fila = []
			for columnas in range(0,320,1):
				x = columnas / (320.0)
				y = filas / (240.0)
				#print x
				punto = nui.SkeletonEngine.depth_image_to_skeleton(x,
																   y,
																   self.depth[filas,
																   columnas, 0])
				if punto.z > 0 and punto.z < self.lim:
					#print 'Este es el limite actual: %f'%(float(lim))
					self.rlt[filas, columnas, 0] = 1
					fila.append(punto)
					#print punto
				else:
					self.rlt[filas, columnas, 0] = 0
			self.nube.add_punto(fila)




