#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan

class problem_6():
	def __init__(self):
		rospy.init_node('sub_lidar2D',anonymous=False)
		rospy.Subscriber("/lidar2D", LaserScan, self.callback)
		rospy.spin()

	def callback(self,data):
		min_range = 10
		min_range_idx = 0
		min_range_degree = 0.0
		#data가 LaserScan 임
		for i,j in enumerate(data.ranges):
			if j < min_range:
				min_range = j
				min_range_idx = i
		min_range_degree = data.angle_min + (min_range_idx * data.angle_increment)

		rospy.loginfo("minimum ranges (%s) angle is %s degree",min_range,min_range_degree)


		
		
if __name__ == '__main__':
	problem_6()