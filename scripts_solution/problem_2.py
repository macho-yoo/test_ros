#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

# ROS Part
def run():
    rospy.init_node("turtle_mover")
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        twist_data = Twist()
        twist_data.linear.x = 0.5
        twist_data.angular.z = 1.0
        pub.publish(twist_data)
        rate.sleep()
        
if __name__ == "__main__":
    run()