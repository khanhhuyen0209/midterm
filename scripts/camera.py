#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Camera_data:
    def __init__(self):
        rospy.init_node('camera', anonymous=False)
        self.bridge = CvBridge() # ham chuyen doi giua OpenCV message va ROS image message
        # lay du lieu dang sensor_msgs/Image tu topic 'robot1/camera1/image_raw' & goi self.image_callback khi co du lieu moi
        self.image_sub = rospy.Subscriber('robot1/camera1/image_raw', Image, self.image_callback)

    def image_callback(self, msg):
        try:
            # chuyen image message tu ROS qua format OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
            cv2.imshow("Camera Feed", cv_image) # in anh qua cua so OpenCV
            cv2.waitKey(1)  # lam moi frame anh
        except Exception as e:
            rospy.logerr("Error processing image: %s", str(e)) # in loi neu co

    def run(self):
        rospy.spin() # giu ct chay lien tuc
        cv2.destroyAllWindows() # don dep + dong cac cua so OpenCV khi ket thuc ct

if __name__ == '__main__':
    try:
        reader = Camera_data()
        reader.run()
    except rospy.ROSInterruptException:
        pass
