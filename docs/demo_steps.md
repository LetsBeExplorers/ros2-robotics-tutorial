# Live Demo

This demo demonstrates a layered ROS 2 architecture implementing reactive obstacle avoidance using TurtleBot3 in Gazebo.

---

## 0. Clean Simulation State

Prevent multiple Gazebo instances:

~~~bash
pkill -9 -f "gz sim"
~~~

---

## 1. Source ROS 2

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

---

## 2. Build and Source Workspace

~~~bash
cd ros2_ws
colcon build
source install/setup.bash
~~~

---

## 3. Set TurtleBot3 Model

~~~bash
export TURTLEBOT3_MODEL=burger
~~~

---

## 4. Launch Simulation World

~~~bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
~~~

Wait until Gazebo fully loads.

---

## 5. Run Perception Node

In a new terminal:

~~~bash
source /opt/ros/jazzy/setup.bash
source ros2_ws/install/setup.bash
ros2 run perception obstacle_avoidance
~~~

Explain:
- Subscribes to `/scan`
- Divides LiDAR into left/front/right sectors
- Publishes `/obstacle_info`

Verify:

~~~bash
ros2 topic echo /obstacle_info
~~~

---

## 6. Run Behavior Node

In another terminal:

~~~bash
source /opt/ros/jazzy/setup.bash
source ros2_ws/install/setup.bash
ros2 run behavior motion_controller
~~~

The robot should begin autonomous navigation.

Explain:
- 10 Hz control loop
- Dual-zone logic (safe / caution / danger)
- Steering based on left-right comparison
- Fully reactive (no map, no global planner)

---

## 7. Inspect Command Velocity

~~~bash
ros2 topic echo /cmd_vel
~~~

Explain:
- Linear velocity depends on front distance
- Angular velocity depends on sector comparison
- Closed-loop control

---

## 8. Demonstrate Reactive Behavior

Drive near:
- Wall
- Pillar
- Corner

Explain:
- Slows in caution zone
- Turns strongly in danger zone
- Continuously adapts to sensor input

---

## 9. Architecture Overview

Pipeline:

/scan  
→ perception (obstacle_avoidance)  
→ /obstacle_info  
→ behavior (motion_controller)  
→ /cmd_vel  
→ robot  

Design principles:
- Layered architecture
- Topic-based communication
- Reactive obstacle avoidance
- Closed-loop control