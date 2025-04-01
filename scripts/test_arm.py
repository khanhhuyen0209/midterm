#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def stop_arm():
    rotation_pub.publish(0.0)
    prismatic_pub.publish(0.0)

def arm_run():
    global rotation_pub, prismatic_pub  # Make publishers accessible in stop_arm()
    
    rospy.init_node('test_arm')

    # Ensure that controllers are ready
    #rospy.wait_for_message('/rotation_controller/command', Float64)
    #rospy.wait_for_message('/prismatic_controller/command', Float64)
    #rospy.loginfo("Controllers detected. Starting command publishing.")

    rotation_pub = rospy.Publisher('/rotation_controller/command', Float64, queue_size=10)
    prismatic_pub = rospy.Publisher('/prismatic_controller/command', Float64, queue_size=10)

    rospy.on_shutdown(stop_arm) # STop arm on shut down 

    # Get positions from parameters -> allow dynamic tuning 
    # ( We can set parameter in launch file/ while running scripts,..
    #  only when the parameter is not set => use ddefault values below )
    rotation_pos = rospy.get_param("~rotation_pos", 1.57) # rad/s
    prismatic_pos = rospy.get_param("~prismatic_pos", 0.01) # meters

    rate = rospy.Rate(50) 
    while not rospy.is_shutdown():
        rotation_pub.publish(rotation_pos)
        prismatic_pub.publish(prismatic_pos)
        rospy.loginfo("Rotation joint position: %.2f rad, Prismatic joint position: %.2f m", rotation_pos, prismatic_pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        arm_run()
    except rospy.ROSInterruptException:
        pass

