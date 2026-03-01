# Live Demo Steps

This document outlines the exact commands and sequence used during the recorded tutorial.

---

## 1. Source ROS 2

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

---

## 2. Set TurtleBot3 Model

TurtleBot3 requires the model type to be set before launching.

~~~bash
export TURTLEBOT3_MODEL=burger
~~~

To make this persistent across terminals:

~~~bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
~~~

Verify:

~~~bash
echo $TURTLEBOT3_MODEL
~~~

Expected output:

~~~
burger
~~~

---

## 3. Launch Simulation World

~~~bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
~~~

Wait for Gazebo to open and ensure simulation is running.

---

## 4. Verify Available Topics

~~~bash
ros2 topic list
~~~

Discuss:
- /cmd_vel
- /scan
- /odom
- /tf

---

## 5. Inspect Command Velocity Topic

~~~bash
ros2 topic info /cmd_vel
~~~

Explain:
- Message type (`TwistStamped`)
- Subscriber count

---

## 6. Move Robot Forward

~~~bash
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"
~~~

Stop with Ctrl+C.

---

## 7. Stop Robot Explicitly

~~~bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"
~~~

Discuss:
- Controllers maintain last velocity.
- Always explicitly send zero to stop.

---

## 8. Rotate Robot to Observe Sensor Changes

~~~bash
ros2 topic pub -r 5 /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.3}}}"
~~~

Open a new terminal:

~~~bash
ros2 topic echo /scan
~~~

Stop rotation with Ctrl+C and send zero velocity.

---

## 9. Inspect LaserScan Data

Discuss:
- `ranges[]` array
- `inf` values (no obstacle detected)
- Finite values (distance in meters)
- How values change as robot rotates or approaches walls