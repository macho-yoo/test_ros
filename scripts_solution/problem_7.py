#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

import math

# ROS Part
class LaserSub(object):
    def __init__(self):
        self.twist_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        rospy.Subscriber("lidar2D", LaserScan, callback=self.laser_sub)
        rospy.Timer(rospy.Duration(0.1), callback=self.cmd_vel_pub)
        self.lidar_data = LaserScan()
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def laser_sub(self, data):
        self.lidar_data = data
   
    def cmd_vel_pub(self, event):
        self.stop_flag = False
        for i, value in enumerate(self.lidar_data.ranges):
            angle = self.lidar_data.angle_min + i * self.lidar_data.angle_increment
            angle_deg = angle * 180 / math.pi
            # print(angle_deg, value)
            # print(-15.0 < angle_deg < 15.0)
            # print(value < 1.0)
            
            if -15.0 < angle_deg < 15.0 and value < 1.0:
                self.stop_flag = True

        if self.stop_flag == True:
            self.stop()
        else:
            self.go_straight()
                    
        
    def go_straight(self):
        rospy.loginfo("go")
        twist_data = Twist()
        twist_data.linear.x = 0.5
        self.twist_pub.publish(twist_data)
        
    def stop(self):
        rospy.loginfo("stop")
        twist_data = Twist()
        twist_data.linear.x = 0
        twist_data.angular.z = 0
        self.twist_pub.publish(twist_data)
        
          
        
        
        
        
        
def run():
    rospy.init_node("LaserSub")
    LaserSub()
    rospy.spin()
    
if __name__ == "__main__":
    run()