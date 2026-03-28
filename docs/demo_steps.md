# Live Demo Flow – ROS 2 Reactive Obstacle Avoidance

## Environment Setup (Intro Section)

### Show System Environment
- Display OS and ROS version
- Confirm ROS is sourced

Commands:
lsb_release -a
ros2 --version

## Workspace & Project Structure

### Show Workspace
- Navigate to workspace
- Explain directory structure

Commands:
cd ros2_ws
tree -L 2

### Explain:
- `src/` → source code and packages
- `build/` → compilation files
- `install/` → executables
- `log/` → build logs

## Build Process

### Build and Source Workspace
- Explain why build is required
- Explain `--symlink-install`

Commands:
colcon build --symlink-install
source install/setup.bash

## Launch System

### Start Simulation
Commands:
./start_sim.sh

- Wait for Gazebo to load

### Start Autonomy Stack
Commands:
./run.sh

- Robot should begin moving

## ROS 2 Core Concepts (While System Running)

### Show Active Topics
Commands:
ros2 topic list

- Explain topics as communication channels

### Inspect LiDAR Data
Commands:
ros2 topic echo /scan

- Explain LaserScan data and ranges

### Inspect Velocity Commands
Commands:
ros2 topic echo /cmd_vel

- Explain linear vs angular velocity

### Inspect Topic Connections
Commands:
ros2 topic info /cmd_vel

### Visualize System
Commands:
rqt_graph

- Show node → topic relationships

## System Behavior Demonstration

### Observe Robot Motion
- Robot moves autonomously
- Explain:
  - Forward motion when clear
  - Turning near obstacles

### Demonstrate Sensor-Driven Behavior
- Move robot near:
  - Walls
  - Corners
  - Tight spaces

Explain:
- Sensor input → decision → motion
- Real-time reactive loop

## Code Walkthrough (Conceptual)

### Perception Node
- Subscribes to `/scan`
- Converts LiDAR into sector distances

### Behavior Node
- Subscribes to processed data
- Applies obstacle avoidance rules
- Publishes motion commands

### Platform Interface Node
- Converts commands into robot motion
- Sends to `/cmd_vel`

## Motion Control Explanation (During Demo)

Commands:
ros2 topic echo /cmd_vel

Explain:
- Linear velocity → forward motion
- Angular velocity → turning
- Values change in real time based on obstacles

## Shutdown

### Stop System
- Safely terminate nodes

Command:
Ctrl + C
