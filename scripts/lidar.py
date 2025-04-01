#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import LaserScan

def lidar_callback(data):
    # Xu ly du lieu lidar
    rospy.loginfo("Receive Lidar's data including %d points,", len(data.ranges)) # In ra so diem 

    if math.isinf(data.ranges[0]) or math.isnan(data.ranges[0]): # Check xem khoang cach toi diem dau tien co hop le khong (co han)
        rospy.loginfo("Invalid first distance (inf or NaN)")
    else:
        rospy.loginfo("First distance: %f meter", data.ranges[0])
if __name__ == '__main__':
    rospy.init_node('lidar')
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    rospy.spin()