#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class problem_7():
	def __init__(self):	
		rospy.init_node('move_car', anonymous=False)
		rospy.Subscriber('/lidar2D',LaserScan,self.callback)
		#self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		#rospy.Timer(rospy.Duration(1.0 / 10), self.timer_CB)
		rospy.spin()

	def callback(self,data):
		self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		front_ranges = data.ranges[90:270]
		if min(front_ranges) < 1 :
			rospy.Timer(rospy.Duration(1.0 / 50), self.timer_CB2)
		rospy.Timer(rospy.Duration(2.0 ), self.timer_CB)
		rospy.loginfo(min(front_ranges))

	def timer_CB(self,event):
		pub_data = Twist()
		pub_data.linear.x = 0.5
		pub_data.angular.z = 0.0
		self.pub.publish(pub_data)
		rospy.loginfo("no stop")

	def timer_CB2(self,event):
		pub_data = Twist()
		pub_data.linear.x = 0.0
		pub_data.angular.z = 0.0
		self.pub.publish(pub_data)
		rospy.loginfo("stoooooopppppp")



	 
if __name__ == '__main__':
	problem_7()
