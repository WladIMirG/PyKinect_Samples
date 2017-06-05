import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

import scipy.io as ScIO
import time
from pykinect.nui import Vector

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

class NubePuntos(object):
	""""""
	nube = {}
	def add_punto(self, punto):
		self.nube[punto.get_coords()] = punto
	def __iter__(self):
		return iter(self.nube)
	def iteritems(self):
		return self.nube.iteritems()

def convertir():
	NewPos = ScIO.loadmat('Nuevos_cursor.mat')['NewPos'][0]
	vec = len (NewPos)
	nube = []
	x = []
	y = []
	z = []

	nub = NubePuntos()
	for i in range(vec):
		punto = Vector(-NewPos[i][0][0][0],
					   NewPos[i][1][0][0],
					   NewPos[i][2][0][0],
					   NewPos[i][3][0][0])
		x.append(float(punto.x))
		y.append(float(punto.y))
		z.append(float(punto.z))
		nube.append(punto)
		nub.add_punto(punto)
	#return nube, nub
	return (x, y, z)
#print 'NUB: ',nub.nube
def animate(i):
	xx0 = []
	xx1 = []
	yy0 = []
	yy1 = []
	zz0 = []
	zz1 = []
	x, z, y = convertir()
	#print i
	for i in range(0,len(x),1):
		if y[i]<1.25 and y[i]>0.3 and z[i]>0:
			yy0.append(y[i])
			zz0.append(z[i])
			xx0.append(x[i])
		elif y[i]<1.25 and y[i]>0.3 and z[i]<0:
			yy1.append(y[i])
			zz1.append(z[i])
			xx1.append(x[i])
	#ax.plot(x,y,z, label='parametric curve')
	ax.scatter(xx0,yy0,zz0, c='g', marker='p')
	ax.scatter(xx1,yy1,zz1, c='r', marker='p')
	#ax.plot_wireframe(x, y, z, rstride=10,cstride=10)
	#ax.plot_surface(x, y, z, rstride=10,cstride=10, alpha=1)

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	ax.legend()
	plt.show()

from OpenGL.GL import *
if __name__ == '__main__':
	a = glVertex4dv((1,2,3,1))
	#ax.plot(x,y,z, label='parametric curve')
	#animate()