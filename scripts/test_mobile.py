#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def stop_robot():
    stop_msg = Twist()
    stop_msg.linear.x = 0.0
    stop_msg.angular.z = 0.0
    pub.publish(stop_msg)  

def run():
    global pub  # Make publisher accessible in stop_robot()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('test_mobile')
    
    rospy.on_shutdown(stop_robot)  # Stop robot on shut down

    rate = rospy.Rate(10)  # 10 Hz
    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.x = 0.5 
        vel.angular.z = 0.2
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass
