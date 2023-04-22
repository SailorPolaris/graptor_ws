#!/usr/bin/env python2
#include "ros/ros.h"

import rospy
import time
import Tkinter as tk
import RPi.GPIO as GPIO
import time
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(data.data)

def listener():
	rospy.init_node('gui_node', anonymous=True)
	rospy.Subscriber("Pressure", String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
