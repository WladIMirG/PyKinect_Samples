# -*- coding: utf-8 -*-
"""
Titulo: imagenDEPTH.py
Descripcion: Esta muestra indica como es el uso de la libreria pykinect para
			extraer la imagen de profundidad del sensor.
Creado: 17/05/2017
@author: Wladimir Garces
"""
import pykinect
from pykinect import nui
from pykinect.nui import Vector

import cv2
import numpy as np


from threading import Thread as Th
#from time import sleep

from recolector import recolector
from graficador2 import graficador
#rec = recolector()

# Iniciar el sensor kinect.
kinect = nui.Runtime()
result = np.empty( ( 240, 320, 1 ), np.uint16 )
rec = recolector()
graf = graficador()
cont = 0
def DEPTH(frame):
	"""Recolecta y dibuja la imagen de profundidad depth
	con las librerias numpy y CV2"""
	global cont
	depth = np.empty(( 240, 320, 1 ), np.uint16)
	frame.image.copy_bits( depth.ctypes.data )
	cv2.imshow( 'VideoDEPTH', depth )
	rec.depth = depth
	rec.recolectar()
	print 'Termine de recolectar'
	#print rec.nube
	graf.cargar_Vertices(rec.nube)

	cv2.imshow( 'VideoDEPTH_RESULT', rec.rlt )
	#sleep(1)



def run():
	""" Asigna la funcion objetivo
	a la variable "depth_frame_ready" del kinect"""
	global kinect
	kinect.camera.elevation_angle = 0
	kinect.skeleton_engine.enabled = True
	kinect.depth_frame_ready += DEPTH
	cv2.namedWindow( 'VideoDEPTH', cv2.WINDOW_AUTOSIZE )
	cv2.namedWindow( 'VideoDEPTH_RESULT', cv2.WINDOW_AUTOSIZE )
	kinect.depth_stream.open( nui.ImageStreamType.Depth, 2,
							  nui.ImageResolution.Resolution320x240,
							  nui.ImageType.Depth )


def wait_key():
	""" Espera que se presione la tecla ESC para que termine
	la ejecucion del programa"""
	while True:
		key = cv2.waitKey(33)
		if key == 27: # ESC
			break
		elif key == 119: # w
			lim += 0.1
		elif key == 115: # s
			lim -= 0.1
	cv2.destroyAllWindows()

def stop():	return kinect.close()

if __name__ == "__main__":

	run()
	graf.main()
	#Th(target=).start()
	wait_key()
	stop()