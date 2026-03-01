# Live Demo Steps

This document outlines the exact commands and sequence used during the recorded tutorial.

---

## 1. Source ROS 2

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

---

## 2. Launch Simulation

~~~bash
ros2 launch turtlebot3_gazebo empty_world.launch.py
~~~

Wait for Gazebo to open and ensure simulation is running.

---

## 3. Verify Available Topics

~~~bash
ros2 topic list
~~~

Discuss:
- /cmd_vel
- /scan
- /odom
- /tf

---

## 4. Inspect Command Velocity Topic

~~~bash
ros2 topic info /cmd_vel
~~~

Explain:
- Message type (TwistStamped)
- Subscriber count

---

## 5. Move Robot Forward

~~~bash
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"
~~~

Stop with Ctrl+C.

---

## 6. Stop Robot

~~~bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"
~~~

---

## 7. Inspect LaserScan Data

~~~bash
ros2 topic echo /scan
~~~

Explain:
- ranges array
- angle_min / angle_max
- obstacle detection concept