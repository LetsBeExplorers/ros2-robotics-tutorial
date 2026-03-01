# ROS 2 Autonomous Navigation Tutorial (Jazzy)

## Overview
This project demonstrates core ROS 2 concepts using a simulated differential drive robot in Gazebo Harmonic.

The tutorial walks through:

- ROS 2 workspace creation and build process (`colcon`)
- Node communication using publishers and subscribers  
- Topic inspection using ROS 2 CLI tools  
- Robot motion control via `/cmd_vel`  
- Sensor data interpretation using LiDAR (`sensor_msgs/LaserScan`)  
- Implementation of reactive obstacle avoidance behavior  
- System visualization using `rqt_graph`  

The goal is to provide a clear, reproducible, hands-on introduction to ROS 2 in a robotics simulation environment.

## System Configuration

- **Operating System:** Ubuntu 24.04 LTS  
- **ROS 2 Distribution:** Jazzy  
- **Simulation Environment:** Gazebo Harmonic (gz sim 8.x)  
- **Robot Type:** Differential drive mobile robot  
- **Primary Sensor:** LiDAR (LaserScan)  

## Installation

### 1. Source ROS 2

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

To verify:

~~~bash
echo $ROS_DISTRO
~~~

Expected output:

~~~
jazzy
~~~

### 2. Install Required Packages

~~~bash
sudo apt update
sudo apt install ros-jazzy-gz-sim ros-jazzy-gz-ros2-control
~~~

(Additional packages will be listed here as development progresses.)

## Workspace Setup

Create a workspace:

~~~bash
mkdir -p ~/ros2_tutorial_ws/src
cd ~/ros2_tutorial_ws
colcon build
~~~

Source the workspace:

~~~bash
source install/setup.bash
~~~

## Build Instructions

From the workspace root:

~~~bash
colcon build
source install/setup.bash
~~~

## Launch Instructions

(Will be finalized once robot integration is complete.)

Example format:

~~~bash
ros2 launch <package_name> <launch_file>.launch.py
~~~

## Reproducing the Demo

1. Source ROS 2:
   ~~~bash
   source /opt/ros/jazzy/setup.bash
   ~~~
2. Build the workspace.  
3. Launch Gazebo simulation.  
4. Run the autonomous behavior node.  
5. Use ROS 2 CLI tools to inspect topics and node communication.  

## Repository Structure

~~~
ros2-robotics-tutorial/
├── ros2_ws/
│   ├── src/
│   ├── build/     (ignored by git)
│   ├── install/   (ignored by git)
│   └── log/       (ignored by git)
│
├── docs/
│   ├── environment_setup.md
│   └── tutorial_outline.md
│
└── README.md
~~~

## Current Status

- ROS 2 Jazzy environment verified  
- Gazebo Harmonic verified  
- Repository structure initialized  
- Robot integration and autonomous behavior in progress  
