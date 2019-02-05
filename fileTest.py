#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

file = open('testfile.txt','a') 
file.write('Hello World') 
file.write('ok daone')
 
file.close() 

return 0

'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
https://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
https://pythonspot.com/matplotlib-update-plot/
http://pythonopencv.com/opencv-real-time-graph-plot-using-matplotlib/
'''
