# Live Demo Steps — ROS 2 Reactive Obstacle Avoidance

This guide lists the exact commands and actions used during the recorded tutorial.

## 1. Show ROS 2 Environment

Display OS and ROS version:

```bash
lsb_release -a
ros2 --version
```

## 2. Show Workspace Structure

```bash
cd ros2_ws
tree -L 2
```

Explain packages and folder organization.

## 3. Build Workspace

```bash
colcon build --symlink-install
source install/setup.bash
```

## 4. Launch Simulation

```bash
./start_sim.sh
```

Wait for Gazebo to fully load.

## 5. Launch Autonomy Stack

Open new terminal:

```bash
./run.sh
```

Robot should begin autonomous movement.

## 6. ROS 2 Core Tools

### List Topics

```bash
ros2 topic list
```

### Inspect LiDAR Sensor

```bash
ros2 topic echo /scan
```

### Inspect Processed Obstacle Data

```bash
ros2 topic echo /obstacle_info
```

### Inspect Velocity Commands

```bash
ros2 topic echo /cmd_vel
```

### View Topic Information

```bash
ros2 topic info /cmd_vel
```

### Visualize ROS Graph

```bash
rqt_graph
```

## 7. Demonstrate Robot Motion Control

Observe robot moving autonomously in Gazebo.

Explain `/cmd_vel` interface:
- Linear velocity controls forward motion
- Angular velocity controls turning

## 8. Demonstrate Sensor-Driven Behavior

Move robot near obstacles:
- Walls
- Corners
- Tight passages

Observe real-time obstacle avoidance.

## 9. Code Walkthrough (No Commands)

Open source files and explain:
- Perception node
- Behavior node
- Platform interface node

## 10. Safe Shutdown

Press:

```
Ctrl + C
```

Scripts safely stop robot and terminate nodes.