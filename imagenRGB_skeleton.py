# -*- coding: utf-8 -*-
"""
Titulo: imagenRGB_skeñeton.py
Descripcion: Esta muestra indica como es el uso de la libreria pykinect para
			extraer la imagen RGB del sensor junto con los puntos del esqueleto.
Creado: 17/05/2017
@author: Wladimir Garces
"""
import pykinect
from pykinect import nui
import cv2
import numpy as np
from IDPuntos import *
from time import sleep
# Iniciar el sensor kinect.
kinect = nui.Runtime()
skeletons = None
video = np.empty(( 480, 640, 4 ), np.uint8)
def comSkeletons(funcion):
	print 'Llego hasta aqui'
	def out(*args, **kwargs):
		global data
		print 'Hasta aqui tambien'
		if skeletons is not None:
			print 'comprobo\n'
			for index, data in enumerate(skeletons):
				if data.eTrackingState != nui.SkeletonTrackingState.TRACKED: continue
				funcion (*args, **kwargs)
		else:
			print 'No comprueba\n'
	return out

@comSkeletons
def manos():
	global video
	for extremidad in SKULL.keys():
		print 
		for junta in SKULL[extremidad]:
			print 'xtremidades: ',extremidad, '\n'+'juntas: ', junta
			Position = data.SkeletonPositions[junta]
			p = nui.SkeletonEngine.skeleton_to_depth_image(Position, 640, 480)
			cv2.circle(video, (int(p[0]), int(p[1])), 5, (255, 0, 0), thickness=5)

def RGB(frame):
	"""Recolecta y dibuja la imagen RGB con las libreria numpy y CV2"""
	global video
	frame.image.copy_bits( video.ctypes.data )
	manos()
	cv2.imshow( 'VideoRGB', video )
	sleep(1)
def skeleton(frame):
    global skeletons
    skeletons = frame.SkeletonData
def run():
	""" Asigana la funcion objetivo
	a la variable "video_frame_ready" del kinect"""
	global kinect
	kinect.skeleton_engine.enabled = True
	kinect.skeleton_frame_ready+=skeleton
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
