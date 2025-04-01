1. Mô phỏng trong Rviz
   rosparam set use_sim_time false
   roslaunch robot1 display.launch
2. Mô phỏng trong Gazebo
   roslaunch robot1 gazebo.launch
   -> In ra dữ liệu camera và LiDAR
   -> rostopic echo /joint_states : in ra dữ liệu encoder
   -> rosrun robot1 test_arm.py : kiểm tra hoạt động tay máy
   -> rosrun robot1 test_mobile.py : kiểm tra hoạt động xe mobile 
