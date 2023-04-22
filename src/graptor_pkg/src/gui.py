#!/usr/bin/env python2
#include "ros/ros.h"

import rospy
import time
import Tkinter as tk
import RPi.GPIO as GPIO
import time
from std_msgs.msg import String

GPIO.setmode(GPIO.BCM)
servo_pins = [2, 3, 4]
solenoid_pins = [5, 6, 7, 8, 9, 10, 11, 12]

for pin in servo_pins:
	GPIO.setup(pin, GPIO.OUT)
for pin in solenoid_pins:
	GPIO.setup(pin, GPIO.OUT)

def callback(data):
	rospy.loginfo(data.data)

def listener():
	rospy.init_node('gui_node', anonymous=True)
	rospy.Subscriber("Pressure", String, callback)
	rospy.spin()










if __name__ == '__main__':
	listener()
