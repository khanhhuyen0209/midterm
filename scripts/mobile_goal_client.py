#!/usr/bin/env python3

import rospy
from srv import mobileGoal

def send_goal(x, y):
    rospy.wait_for_service('go_to_goal')
    try:
        go_to_goal = rospy.ServiceProxy('go_to_goal', mobileGoal)
        response = go_to_goal(x, y)
        if response.success:
            rospy.loginfo(" Reach goal successfully! ")
        else:
            rospy.loginfo(" Fail to reach goal! ")
    except rospy.ServiceException as e:
        rospy.logerr("Error calling service: %s", e)

if __name__ == '__main__':
    rospy.init_node('go_to_goal_client')
    x_goal = float(input("Nhap X: "))
    y_goal = float(input("Nhap Y: "))
    send_goal(x_goal, y_goal)