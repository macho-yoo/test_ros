#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from visualization_msgs.msg import MarkerArray, Marker
import random


class problem_4():
	def __init__(self):
		rospy.init_node("THREE_MARKER")
		self.publisher = rospy.Publisher("visualization_marker_array",MarkerArray, queue_size=10)
		rospy.Timer(rospy.Duration(1.0 / 10.0), self.timer_CB)
		rospy.spin()

	def timer_CB(self,event):
		pub_data = MarkerArray()

		r_lst = [0.1,0.2,0.3,0.4,0.5]
		g_lst = [0.5,0.4,0.3,0.2,0.1]
		b_lst = [0.3,0.7,0.5,0.06,0.2]
		for i in range(1,4):
			tmp_data = Marker()

			tmp_data.header.stamp = rospy.Time.now()
			tmp_data.header.frame_id = 'base_link'

			tmp_data.type = i
			tmp_data.id = i+1
			tmp_data.pose.position.x = 3*i
			tmp_data.pose.position.y = 3*1
			tmp_data.pose.position.z = 0

			tmp_data.pose.orientation.x = 0
			tmp_data.pose.orientation.y = 0
			tmp_data.pose.orientation.z = 0
			tmp_data.pose.orientation.w = 0

			tmp_data.scale.x = i
			tmp_data.scale.y = i
			tmp_data.scale.z = i

			tmp_data.color.r = r_lst[random.randint(0,4)]
			tmp_data.color.g = g_lst[random.randint(0,4)]
			tmp_data.color.b = b_lst[random.randint(0,4)]
			tmp_data.color.a = 1

			pub_data.markers.append(tmp_data)



		self.publisher.publish(pub_data)

if __name__=='__main__':
	problem_4()