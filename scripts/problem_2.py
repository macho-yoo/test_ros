#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class problem_2():
	def __init__(self):	
		rospy.init_node('move_turtle', anonymous=False)
		self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		rospy.Timer(rospy.Duration(1.0 / 10), self.timer_CB)
		rospy.spin()

	def timer_CB(self,event):
		pub_data = Twist()
		pub_data.linear.x = 0.5
		pub_data.angular.z = 1.0

		self.pub.publish(pub_data)



	 
if __name__ == '__main__':
	problem_2()
