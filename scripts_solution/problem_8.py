#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import math

# ROS Part
class TurtleMover(object):
    def __init__(self):
        self.goal_pose = Pose()

        self.turtle_pose = Pose()
        
        self.goal_flag = True
        self.twist_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1)
        rospy.Subscriber("turtle1/pose", Pose, callback=self.pose_sub)
        rospy.Timer(rospy.Duration(0.05), callback=self.move_turtle)
        
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def pose_sub(self, data):
        self.turtle_pose = data
        # rospy.loginfo(data)
        
        
    def move_turtle(self, event):
    
        if self.goal_flag == True:
            self.goal_pose.x = float(raw_input("print goal x : "))
            self.goal_pose.y = float(raw_input("print goal y : "))
            self.goal_flag = False
        else:
            self.target_yaw = math.atan2(self.goal_pose.y - self.turtle_pose.y, self.goal_pose.x - self.turtle_pose.x)
            # - pi ~ + pi

            print("yaw_diff = ", abs(self.turtle_pose.theta - self.target_yaw))
            print("distance = ", self.calc_dist())
            if abs(self.turtle_pose.theta - self.target_yaw) > 0.05:
                self.turtle_turn()
            
            # else:
            #     self.turtle_stop()
                
            elif self.calc_dist() > 0.05:
                self.turtle_go()
                
                # standard_time = rospy.Time.now()
                
            else:
                self.turtle_stop()
                self.goal_flag = True
        
        
    def calc_dist(self):
        x_diff = self.turtle_pose.x - self.goal_pose.x
        # print("x_diff", x_diff)
        y_diff = self.turtle_pose.y - self.goal_pose.y
        # print("y_diff", y_diff)
        
        return (x_diff ** 2 + y_diff ** 2) ** 0.5
            

            
            
    def turtle_turn(self):
        rospy.loginfo("turn")
        
        twist_data = Twist()
        twist_data.angular.z = 0.3
        self.twist_pub.publish(twist_data)
        
    def turtle_go(self):
        rospy.loginfo("go straight")
        twist_data = Twist()
        twist_data.linear.x = 0.5
        self.twist_pub.publish(twist_data)
        
    
    def turtle_stop(self):
        rospy.loginfo("stop")
        
        twist_data = Twist()
        self.twist_pub.publish(twist_data)
        
        
        
        
        
        
def run():
    rospy.init_node("polygoner")
    TurtleMover()
    rospy.spin()
    
if __name__ == "__main__":
    run()