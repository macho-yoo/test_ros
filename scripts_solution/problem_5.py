#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose


# ROS Part
class PoseSub(object):
    def __init__(self):
        rospy.Subscriber("turtle1/pose", Pose, callback=self.pose_sub)
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def pose_sub(self, data):
        rospy.loginfo("(x, y, theta) = ({}, {}, {})".format(data.x, data.y, data.theta))
        
        
        
        
        
        
        
def run():
    rospy.init_node("polygoner")
    PoseSub()
    rospy.spin()
    
if __name__ == "__main__":
    run()