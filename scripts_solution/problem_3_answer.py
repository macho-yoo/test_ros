#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PolygonStamped, Point32

import math

# ROS Part
class Polygoner(object):
    def __init__(self):
        self.polygon_publisher = rospy.Publisher("star", PolygonStamped, queue_size=1)
        rospy.Timer(rospy.Duration(1.0), self.timer_star)
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def timer_star(self, event):
        star_polygon = PolygonStamped()
        star_polygon.header.stamp = rospy.Time.now()
        star_polygon.header.frame_id = "star"
        r = 5
        point1 = Point32()
        point1.x = r * math.cos(72. / 180 * math.pi)
        point1.y = r * math.sin(72. / 180 * math.pi)
        
        point2 = Point32()
        point2.x = r * math.cos(72. * 2 / 180 * math.pi)
        point2.y = r * math.sin(72. * 2 / 180 * math.pi)
        point3 = Point32()
        point3.x = r * math.cos(72. * 3 / 180 * math.pi)
        point3.y = r * math.sin(72. * 3/ 180 * math.pi)
        point4 = Point32()
        point4.x = r * math.cos(72. * 4 / 180 * math.pi)
        point4.y = r * math.sin(72. * 4 / 180 * math.pi)
        point5 = Point32()
        point5.x = r * math.cos(72. * 5 / 180 * math.pi)
        point5.y = r * math.sin(72. * 5 / 180 * math.pi)
        
        star_polygon.polygon.points.append(point1)
        star_polygon.polygon.points.append(point3)
        star_polygon.polygon.points.append(point5)
        star_polygon.polygon.points.append(point2)
        star_polygon.polygon.points.append(point4)
        
        # star_polygon.polygon.points.append(point1)
        # star_polygon.polygon.points.append(point2)
        # star_polygon.polygon.points.append(point3)
        # star_polygon.polygon.points.append(point4)
        # star_polygon.polygon.points.append(point5)
        self.polygon_publisher.publish(star_polygon)
        rospy.loginfo("publish")
        
        
        
        
        
        
        
        
def run():
    rospy.init_node("polygoner")
    Polygoner()
    rospy.spin()
    
if __name__ == "__main__":
    run()