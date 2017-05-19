# -*- coding: utf-8 -*-
"""
Titulo: imagenRGB.py
Descripcion: Esta muestra indica como es el uso de la libreria pykinect para
			extraer la imagen RGB del sensor.
Creado: 17/05/2017
@author: Wladimir Garces
"""
import pykinect
from pykinect import nui
import cv2
import numpy as np

# Iniciar el sensor kinect.
kinect = nui.Runtime()

def DEPTH(frame):
	"""Recolecta y dibuja la imagen de profundidad depth
	con las librerias numpy y CV2"""
	depth = np.empty(( 240, 320, 1 ), np.uint16)
	frame.image.copy_bits( depth.ctypes.data )
	cv2.imshow( 'VideoDEPTH', depth )

def run():
	""" Asigna la funcion objetivo
	a la variable "depth_frame_ready" del kinect"""
	global kinect 
	kinect.depth_frame_ready += DEPTH
	kinect.depth_stream.open( nui.ImageStreamType.Depth, 2,
							  nui.ImageResolution.Resolution320x240,
							  nui.ImageType.Depth )
	cv2.namedWindow( 'VideoDEPTH', cv2.WINDOW_AUTOSIZE )

def wait_key():
	""" Espera que se presione la tecla ESC para que termine
	la ejecucion del programa"""
	while True:
		key = cv2.waitKey(33)
		if key == 27: # ESC
			break
	cv2.destroyAllWindows()

def stop():	return kinect.close()

if __name__ == "__main__":

	run()
	wait_key()
	stop()
