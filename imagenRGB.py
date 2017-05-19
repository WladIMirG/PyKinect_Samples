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

def RGB(frame):
	"""Recolecta y dibuja la imagen RGB con las libreria numpy y CV2"""
	video = np.empty(( 480, 640, 4 ), np.uint8)
	frame.image.copy_bits( video.ctypes.data )
	cv2.imshow( 'VideoRGB', video )

def run():
	""" Asigana la funcion objetivo
	a la variable "video_frame_ready" del kinect"""
	global kinect 
	kinect.video_frame_ready += RGB 
	kinect.video_stream.open( nui.ImageStreamType.Video, 2,
							  nui.ImageResolution.Resolution640x480,
							  nui.ImageType.Color )
	cv2.namedWindow( 'VideoRGB', cv2.WINDOW_AUTOSIZE )

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
