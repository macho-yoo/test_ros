#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray


# ROS Part
class MarkerClass(object):
    def __init__(self):
        self.marker_array_publisher = rospy.Publisher("markers", MarkerArray, queue_size=1)
        rospy.Timer(rospy.Duration(0.5), self.marker_array)
        self.color_array = [[1.0, 0.0, 0.0, 1.0],
                            [1.0, 0.5, 0.0, 1.0],
                            [1.0, 1.0, 0.0, 1.0],
                            [0.0, 1.0, 0.0, 1.0],
                            [0.0, 0.0, 1.0, 1.0],
                            [0.33, 0.0, 0.5, 1.0],
                            [0.5, 0.0, 0.5, 1.0]]
        
        self.count = 0
        
    #==========================================================
    #                   Callback Function
    #==========================================================
    
    def marker_array(self, event):
        markers = MarkerArray()
        marker1 = Marker()
        marker2 = Marker()
        marker3 = Marker()
        marker1.header.stamp = rospy.Time.now()
        marker1.header.frame_id = "marker"
        marker1.id = 1
        marker1.type = 1
        marker1.pose.position.x = 0.0
        marker1.pose.position.y = 0.0
        marker1.pose.position.z = 0.0
        marker1.scale.x = 1.0
        marker1.scale.y = 1.0
        marker1.scale.z = 1.0
        marker1.color.r = self.color_array[self.count][0]
        marker1.color.g = self.color_array[self.count][1]
        marker1.color.b = self.color_array[self.count][2]
        marker1.color.a = self.color_array[self.count][3]
        
        marker2.header.stamp = rospy.Time.now()
        marker2.header.frame_id = "marker"
        marker2.id = 2
        marker2.type = 0
        marker2.pose.position.x = 3.0
        marker2.pose.position.y = 3.0
        marker2.pose.position.z = 3.0
        marker2.scale.x = 1.0
        marker2.scale.y = 1.0
        marker2.scale.z = 1.0
        marker2.color.r = self.color_array[self.count][0]
        marker2.color.g = self.color_array[self.count][1]
        marker2.color.b = self.color_array[self.count][2]
        marker2.color.a = self.color_array[self.count][3]
        
        marker3.header.stamp = rospy.Time.now()
        marker3.header.frame_id = "marker"
        marker3.id = 3
        marker3.type = 3
        marker3.pose.position.x = -3.0
        marker3.pose.position.y = -3.0
        marker3.pose.position.z = -3.0
        marker3.scale.x = 1.0
        marker3.scale.y = 1.0
        marker3.scale.z = 1.0
        marker3.color.r = self.color_array[self.count][0]
        marker3.color.g = self.color_array[self.count][1]
        marker3.color.b = self.color_array[self.count][2]
        marker3.color.a = self.color_array[self.count][3]
        
        
        
        
        
        
        markers.markers.append(marker1)
        markers.markers.append(marker2)
        markers.markers.append(marker3)
        self.marker_array_publisher.publish(markers)
        rospy.loginfo("publish")
        self.count += 1
        self.count = self.count % 7
        
        
        
        
        
        
        
        
def run():
    rospy.init_node("polygoner")
    MarkerClass()
    rospy.spin()
    
if __name__ == "__main__":
    run()