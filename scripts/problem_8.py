#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import numpy as np 
import cv2 as cv2


class problem_8():
	def __init__(self):
		rospy.init_node('sub_turtle_pos2', anonymous=False)
		self.x = int(raw_input())
		self.y = int(raw_input())
		rospy.Subscriber("/turtle1/pose", Pose, self.callback)
		#self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
		#rospy.Timer(rospy.Duration(1.0 / 10), self.timer_CB)
		rospy.spin()

	def callback(self,data):
		#rospy.loginfo("(x,y,theta) = (%s,%s,%s)",data.x,data.y,data.theta)

		self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

		point1 = [data.x,data.y]
		point2 = [self.x,self.y]


		theta = self.getAngle2P(point1,point2)
		pub_data = Twist()

		pub_data.linear.x = self.calc_dist(point1,point2) / 5
		pub_data.angular.z = theta
		rospy.loginfo(theta)

		self.pub.publish(pub_data)
		

	#def timer_CB(self,event):

		#pub_data = Twist()
		#pub_data.linear.x = 0.5
		#pub_data.angular.z = 1.0

		#self.pub.publish(pub_data)

	def getAngle2P(self, p1, p2, direction="CW"):  
		ang1 = np.arctan2(*p1[::-1])
		ang2 = np.arctan2(*p2[::-1])
		res = np.rad2deg((ang1 - ang2) % (2 * np.pi))
		return res

	def calc_dist(self,p1,p2):
		result = math.sqrt(math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2))
		return result
		





if __name__ == '__main__':
	problem_8()