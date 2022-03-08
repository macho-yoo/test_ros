#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def turtle_pos():
	rospy.init_node('sub_turtle_pos', anonymous=False)
	rospy.Subscriber("/turtle1/pose", Pose, callback)
	rospy.spin()

def callback(data):
	rospy.loginfo("(x,y,theta) = (%s,%s,%s)",data.x,data.y,data.theta)

if __name__ == '__main__':
	turtle_pos()
	