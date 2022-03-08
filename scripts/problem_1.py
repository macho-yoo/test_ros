#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class problem_1():
	def __init__(self):
		rospy.init_node('pub_string')
		self.pub = rospy.Publisher('new_msg',String,queue_size=1)
		rospy.Timer(rospy.Duration(1.0), self.timer_CB)
		rospy.spin()

	def timer_CB(self, event):
		pub_data = String()
		pub_data.data = "Today is 2022-03-08, Hello World"
		self.pub.publish(pub_data)

if __name__=="__main__":
	problem_1()
