#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def run():
    rospy.init_node("msg_node")
    pub = rospy.Publisher("new_msg", String, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        string_data = String()
        string_data.data = "Today is 2022-03-08, Hello World"
        pub.publish(string_data)
        rate.sleep()
        
if __name__ == "__main__":
    run()