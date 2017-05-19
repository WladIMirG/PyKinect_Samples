# -*- coding: utf-8 -*-

import numpy
import sklearn
from sklearn import datasets
#help('sklearn')base

data = datasets.load_digits()

print data.data
print data.target

print 'hola'
import pypot
#import pypot.kinematics.Chain as ch
#ch.forward_kinematics(45, 45, 10)
#pypot.sensor.camera()
help('pypot')
help('pypot.sensor.kinect')