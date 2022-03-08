#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

import math

# ROS Part
class LaserSub(object):
    def __init__(self):
        rospy.Subscriber("lidar2D", LaserScan, callback=self.laser_sub)
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def laser_sub(self, data):
        # min_range = min(data.ranges)
        # min_index = data.ranges.index(min_range)
        # min_range_angle = data.angle_min + min_index * data.angle_increment
        
        # rospy.loginfo("minimum ranges' ({}m) angle is {} degree".format(min_range, min_range_angle * 180 / math.pi))
        
        min_range = data.range_max ## 10.0 m
        min_index = 0
        for i, value in enumerate(data.ranges):
            if value < min_range:
                min_range = value
                min_index = i
        min_range_angle = data.angle_min + min_index * data.angle_increment
                
        rospy.loginfo("minimum ranges' ({}m) angle is {} degree".format(min_range, min_range_angle * 180 / math.pi))
        
        
def run():
    rospy.init_node("LaserSub")
    LaserSub()
    rospy.spin()
    
if __name__ == "__main__":
    run()