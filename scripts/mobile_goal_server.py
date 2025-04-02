#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from srv import mobileGoal, mobileGoalResponse
import tf.transformations as tf_trans  # Import for quaternion conversion

current_pose = Odometry()

def odom_callback(msg):
    global current_pose
    current_pose = msg  
    rospy.sleep(1)

# Function to convert quaternion to yaw (θ)
def get_yaw_from_quaternion(quaternion):
    _, _, yaw = tf_trans.euler_from_quaternion([
        quaternion.x, quaternion.y, quaternion.z, quaternion.w
    ])
    return yaw

# Move robot to goal
def go_to_goal(req):
    global current_pose
    goal_x, goal_y = req.x, req.y
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    vel_msg = Twist()

    # Ensure odometry is received before proceeding
    while current_pose.header.stamp == rospy.Time(0):  # Check if timestamp is zero (uninitialized)
        rospy.logwarn("Waiting for odometry data...")
        rospy.sleep(1)

    while not rospy.is_shutdown():
        # Get current position
        current_x = current_pose.pose.pose.position.x
        current_y = current_pose.pose.pose.position.y
        current_theta = get_yaw_from_quaternion(current_pose.pose.pose.orientation)

        # Compute distance to goal
        distance = math.sqrt((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2)

        # Compute angle to goal
        angle_to_goal = math.atan2(goal_y - current_y, goal_x - current_x)
        angle_error = angle_to_goal - current_theta

        # Normalize angle error to [-π, π]
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        # Move towards goal
        vel_msg.linear.x = min(1.0, distance)  # Limit max speed
        vel_msg.angular.z = 2.0 * angle_error  # Adjust rotation
        
        # Stop if goal is reached
        if distance < 0.1:
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            pub.publish(vel_msg)
            return mobileGoalResponse(success=True)
        
        pub.publish(vel_msg)
        rate.sleep()

# Initialize service
def go_to_goal_server():
    rospy.init_node('go_to_goal_server')
    rospy.Subscriber("/odom", Odometry, odom_callback)
    rospy.Service('go_to_goal', mobileGoal, go_to_goal)
    rospy.spin()

if __name__ == '__main__':
    go_to_goal_server()

