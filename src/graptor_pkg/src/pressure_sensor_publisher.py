#!/usr/bin/env python2

import rospy
import serial
import time
from std_msgs.msg import Int32

#include "ros/ros.h"

def talker():
#	ser = serial.Serial('/dev/ttyACM0', 115200)
#	time.sleep(0.1)
#	pressure_read = ser.readline()
#	pressure_d = pressure_read.decode()
#	pressure = pressure_d.rstrip()
#
	pub = rospy.Publisher('Pressure', Int32, queue_size = 10)
	rospy.init_node('pressure_node', anonymous = True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		ser = serial.Serial('/dev/ttyACM0', 115200)
		time.sleep(0.1)
		pressure_read = ser.readline()
		pressure_d = pressure_read.decode()
		pressure = pressure_d.rstrip()
		
		rospy.loginfo(pressure)
		pub.publish(pressure)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
