# -*- coding: utf-8 -*-

import pykinect
from pykinect import nui
import cv2
import numpy as np
from time import sleep

class kinect():
    def __init__(self):
        self.Runtime = nui.Runtime()
        hol = 'Hola'
        print hol

    def Run(self):
        
        self.Runtime.video_frame_ready += self.Camara_RGB
        self.Runtime.depth_frame_ready += self.Camara_DEPTH

        cv2.namedWindow( 'video', cv2.WINDOW_AUTOSIZE )
        cv2.namedWindow( 'depth', cv2.WINDOW_AUTOSIZE )

        self.Runtime.video_stream.open( nui.ImageStreamType.Video, 2,
                                        nui.ImageResolution.Resolution640x480,
                                        nui.ImageType.Color )
        self.Runtime.depth_stream.open( nui.ImageStreamType.Depth, 2,
                                        nui.ImageResolution.Resolution320x240,
                                        nui.ImageType.Depth )

    def close(self):
        return self.Runtime.close()

    def Camara_RGB(self, frame):
        video = np.empty( ( 480, 640, 4 ), np.uint8 )
        frame.image.copy_bits( video.ctypes.data )
        
        cv2.imshow( 'video', video )

    def Camara_DEPTH(self, frame):
        depth = np.empty( ( 240, 320, 1 ), np.uint16 )
        frame.image.copy_bits( depth.ctypes.data )
        
        cv2.imshow( 'depth', depth )

    def desactivar(self):
        while True:
    #waitKey() returns ASCII code of the pressed key
            key = cv2.waitKey(33)
            if key == 27: # ESC
                break
            elif key == 118: # 'v'
                print >> sys.stderr, "Video stream activated"
                videoDisplay = True
            elif key == 100: # 'd'
                print >> sys.stderr, "Depth stream activated"
                videoDisplay = False
        self.close()

if __name__ == '__main__':
    from time import sleep
    kin = kinect()
    kin.Run()
    kin.desactivar()
    #kin.camera.elevation_angle = 15
    print 'Ya cerré'
    