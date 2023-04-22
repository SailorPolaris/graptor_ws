#!/usr/bin/env python2
#include "ros/ros.h"

import rospy
import time
import Tkinter as tk
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard this", data.data)

def listener():
	rospy.init_node('gui_node', anonymous=True)
	rospy.Subscriber("Pressure", Int32, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
