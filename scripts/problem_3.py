#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import PolygonStamped
from geometry_msgs.msg import Point32
import math




class problem_3():
    def __init__(self):
        rospy.init_node("star_drawer")
        self.publisher = rospy.Publisher("star_polygon", PolygonStamped, queue_size=10)
        rospy.Timer(rospy.Duration(1.0 / 10.0), self.timer_CB)
        rospy.spin()

    def timer_CB(self,event):
        pub_data = PolygonStamped()
        pub_data.header.stamp = rospy.Time.now()
        pub_data.header.frame_id = "base_link"

        ######polygonstamped 안에 polygon 채우기

        tmp_point = Point32()

        for i in range(2000):
            tmp_point = Point32()
            tmp_point.x =  (5 * math.cos(2* i)) + (2 * math.cos(3*i))
            tmp_point.y = (2*math.sin(3*i)) - (5*math.sin(2*i))
            tmp_point.z = 0
            pub_data.polygon.points.append(tmp_point)

        print(pub_data.polygon.points)

        self.publisher.publish(pub_data)


if __name__=='__main__':
    problem_3()