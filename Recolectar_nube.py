# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 16:01:43 2014

@author: IngGarces
"""


import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.io as ScIO
import cv2
import numpy as np
import pykinect
from pykinect import nui
import thread
import sys
from time import sleep
#import pcl

global cloundpoint
# Video
def video_frame_ready( frame ):
    if videoDisplay == False: return

    with screenLock:
        video = np.empty( ( 480, 640, 4 ), np.uint8 )
        frame.image.copy_bits( video.ctypes.data )
        print 'esto es video: ', video[1]

        if skeletons is not None:
            for index, data in enumerate(skeletons):
                if data.eTrackingState != nui.SkeletonTrackingState.TRACKED: continue

                #get right hand position
                handRightPosition = data.SkeletonPositions[nui.JointId.HandRight]
                hr = nui.SkeletonEngine.skeleton_to_depth_image(handRightPosition, 640, 480)

                #get left hand position
                handLeftPosition = data.SkeletonPositions[nui.JointId.HandLeft]
                hl = nui.SkeletonEngine.skeleton_to_depth_image(handLeftPosition, 640, 480)

                print "(%d, %d)" % (int(hr[0]), int(hr[1]))
                cv2.circle(video, (int(hr[0]), int(hr[1])), 20, (255, 0, 0), thickness=10)
                cv2.circle(video, (int(hl[0]), int(hl[1])), 20, (0, 0, 255), thickness=10)

        cv2.imshow( 'frame', video )
        sleep(1)
def guardar(Dato):
    ScIO.savemat('Nuevos_cursor.mat', mdict={'NewPos': Dato})

# Depth
def depth_frame_ready( frame ):
    if videoDisplay == True: return

    depth = np.empty( ( 240, 320, 1 ), np.uint16 )
    depth1 = np.empty( ( 240, 320, 1 ), np.uint16 )
    frame.image.copy_bits( depth.ctypes.data )
    #print 'esto es depth: ', depth[240-1,320-1,0]
    k = 0.1236# milimetros
#    x = np.empty( ( 240, 320), np.uint16 )
#    y = np.empty( ( 240, 320), np.uint16 )
#    z = 
    cloundpoint = []#np.empty( ( 240, 320), np.uint16 )
    X = []
    Y = []
    Z = []
# 2842.5
    depth1 = k*np.tan(((depth/2842.5)+1.1863)) - 0.037
    for columnas in range(0,320,1):
        for filas in range(0,240,1):

            x = columnas / 320.0
            y = filas / 240.0
            punto = nui.SkeletonEngine.depth_image_to_skeleton(x, y, depth[filas, columnas, 0])
            #print nn

            if punto.z > 0.5 and punto.z < 1.2:
                depth1[filas, columnas, 0] = 1
                X.append(punto.x)
                Y.append(punto.y)
                Z.append(punto.z)
                cloundpoint.append(punto)
                #print nn
                #print '<X: %f, Y: %f, Z: %f> <X-columnas: %d, Y-filas: %d>'%(nn.x,nn.y,nn.z,columnas,filas)
            else:
                depth1[filas, columnas, 0] = 0

    #for i in range(0,100,1): print 'vector: ', cloundpoint[i]
    guardar(cloundpoint)
    


            #print '<X: %f, Y: %f, Z: %f> <X-columnas: %d, Y-filas: %d>'%(x,y,z,columnas,filas)
        #sleep(0.01)

    #print depth[200,10,0]
    #print depth1

    # print skeletons
    # if skeletons is not None:
    #     for index, data in enumerate(skeletons):
    #         if data.eTrackingState != nui.SkeletonTrackingState.TRACKED: continue
    #         #get head position
    #         headPosition = data.SkeletonPositions[nui.JointId.Head]
    #         hp = nui.SkeletonEngine.skeleton_to_depth_image(headPosition, 320, 240)

    #         cv2.circle(depth, (int(hp[0]), int(hp[1])), 20, (255, 255, 255), thickness=10)

    cv2.imshow( 'frame', depth )
    cv2.imshow( 'frame1', depth1 )
    sleep(5)
    
def skeleton_frame_ready(frame):
    global skeletons
    skeletons = frame.SkeletonData

if __name__ == '__main__':
    screenLock = thread.allocate()

    videoDisplay = False

    kinect = nui.Runtime()
    kinect.camera.elevation_angle = -5

    skeletons = None

    #skeleton frame ready event handling
    #Reference : http://www.slideshare.net/pycontw/pykinect
    kinect.skeleton_engine.enabled = True

    kinect.skeleton_frame_ready += skeleton_frame_ready
    kinect.video_frame_ready += video_frame_ready
    kinect.depth_frame_ready += depth_frame_ready

    kinect.video_stream.open( nui.ImageStreamType.Video, 2, nui.ImageResolution.Resolution640x480, nui.ImageType.Color )
    kinect.depth_stream.open( nui.ImageStreamType.Depth, 2, nui.ImageResolution.Resolution320x240, nui.ImageType.Depth )

    cv2.namedWindow( 'frame', cv2.WINDOW_AUTOSIZE )
    cv2.namedWindow( 'frame1', cv2.WINDOW_AUTOSIZE )
    #cv2.namedWindow( 'frame2', cv2.WINDOW_AUTOSIZE )
    plt.show()
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

    cv2.destroyAllWindows()
    kinect.close()