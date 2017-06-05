from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pykinect.nui import Vector
import sys
#from time import sleep
from numpy import absolute
class graficador:
	Xp = 0.7 #metro
	Yp = 1.0 #metro
	d = 0.01 #metro
	n = -1

	edges = []
	verts = []
	surfaces = []

	def __init__(self):
		self.calc()
	def calc(self):
		dx = self.Xp/2
		dy = self.Yp/2
		x = -dx
		y = dy
		z = 0
		fila = []
		for filas in range(int(self.Yp/self.d)):
			x = -dx
			#print x, y
			y = y - self.d
			for columnas in range(int(self.Xp/self.d)):
				
				fila.append(Vector(x,y,z))
				x = x + self.d
				#sleep(0.0001)
				
			self.verts.append(fila)
			fila = []

		#print self.verts

	def InitGL(self,Width,Height):
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0) 
		glDepthFunc(GL_LESS) 
		#glShadeModel(GL_SMOOTH)   
	 	glMatrixMode(GL_PROJECTION)
	 	glLoadIdentity()
	 	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	 	glMatrixMode(GL_MODELVIEW)
	def dibujar(self):
		#glRotatef(-90, 1, 0, 0)
		if self.verts is not None:
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT )
			self.surface(GL_POINTS)
			self.verts = None
		#glutSwapBuffers()

	def cargar_Vertices(self, verts):
		self.verts = verts

	def cargar_Edges(self, edges):
		self.edges = edges

	def cargar_Surfaces(self, *args):
	#	for i in *args:
	#		if i == 
		pass
	def surface(self, i):
		#glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		if i == GL_QUADS:
			pass
		if i == GL_TRIANGLES:
			pass
		if i == GL_LINES:
			pass
			#glBegin(mode)
			#for edge in self.edges:
			#	for vertice in edge:
			#		glVertex3fv(self.verts[vertice])
			#glEnd()
		if i == GL_POINTS:
			glBegin(i)
			self.n += 1
			#glColor((self.n+1,self.n+1,self.n+1))
			for fila in self.verts:
				for punto in fila:
					#print 'punto: ', punto.get_coords
					glVertex3fv((punto.x, punto.y, punto.z))
			
			#print 'Voliv a dibujar lo mismo: ',self.n
			glEnd()

		glutSwapBuffers()
		#glRotatef(15,1,0,0)
		#sleep(0.05)
	def main(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(600,600)
		glutInitWindowPosition(200,100)        

		window = glutCreateWindow('OpenGL')

		glTranslatef(0.0,0.0,-3)
		#glRotatef(-90, -1, 0, 0)

		glutDisplayFunc(self.dibujar)
		glutIdleFunc(self.dibujar)
		self.InitGL(600, 600)
		glutMainLoop()