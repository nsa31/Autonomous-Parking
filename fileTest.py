#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

file = open('testfile.txt','a') 
file.write('Hello World') 
file.write('ok daone')
 
file.close() 
