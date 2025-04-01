cmake_minimum_required(VERSION 2.8.3)

project(robot1)

find_package(catkin REQUIRED
gazebo_ros
gazebo_plugins
sensor_msgs
urdf
hardware_interface
controller_manager
joint_state_publisher
joint_state_publisher_gui
position_controllers
rospy
tf
std_msgs
image_transport
camera_info_manager
cv_bridge
nav_msgs
message_generation
)

add_service_files(
  FILES
  mobileGoal.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package( CATKIN_DEPENDS 
gazebo_ros 
gazebo_plugins 
sensor_msgs 
hardware_interface 
controller_manager 
joint_state_publisher 
joint_state_publisher_gui
position_controllers
rospy
tf
std_msgs
urdf
image_transport
camera_info_manager
cv_bridge
nav_msgs
message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/mobile_goal_server.py scripts/mobile_goal_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

