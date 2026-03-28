# ROS 2 Autonomous Navigation Tutorial (Jazzy)

## Overview

This project demonstrates foundational ROS 2 robotics concepts using a simulated TurtleBot3 differential drive robot in Gazebo Harmonic.

The tutorial focuses on building a simple, modular autonomy stack that implements basic reactive obstacle avoidance.  
The behavior is intentionally designed using straightforward rule-based logic rather than advanced planning algorithms in order to emphasize core ROS 2 principles and system integration.

Topics covered include:

- ROS 2 workspace creation and build process (`colcon`)
- Node communication using publishers and subscribers
- Topic inspection using ROS 2 CLI tools
- Robot motion control via `/cmd_vel`
- Sensor data interpretation using LiDAR (`sensor_msgs/LaserScan`)
- Implementation of reactive obstacle avoidance behavior
- System visualization using `rqt_graph`
- Modular robotics system design (perception → behavior → platform)

The goal is to provide a clear, reproducible robotics tutorial in a simulation-first environment.

## Quick Start (Run the Demo)

If dependencies are already installed, you can launch the full system with:

~~~bash
# Clone the repository
git clone https://github.com/LetsBeExplorers/ros2-robotics-tutorial.git
cd ros2-robotics-tutorial

# Source ROS 2
source /opt/ros/jazzy/setup.bash

# Build workspace
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
cd ..

# Make scripts executable (first time only)
chmod +x start_sim.sh run.sh

# Start simulator
./start_sim.sh

# In a new terminal, start autonomy
./run.sh
~~~

The TurtleBot3 robot will begin autonomous obstacle avoidance in Gazebo.

For full installation and setup instructions, see sections below.

## System Configuration

- **Operating System:** Ubuntu 24.04 LTS  
- **ROS 2 Distribution:** Jazzy  
- **Simulation Environment:** Gazebo Harmonic (`gz sim` 8.x)  
- **Robot Platform:** TurtleBot3 Burger  
- **Robot Type:** Differential drive mobile robot  
- **Primary Sensor:** LiDAR (`LaserScan`)  

## Installation

### 1. Install ROS 2 Jazzy

Follow the official ROS 2 Jazzy installation guide for Ubuntu 24.04.

After installation:

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

Verify:

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
sudo apt install ros-jazzy-gz-sim ros-jazzy-gz-ros2-control ros-jazzy-ros-gz-bridge ros-jazzy-turtlebot3*
~~~

### 3. Set TurtleBot3 Model

~~~bash
export TURTLEBOT3_MODEL=burger
~~~

(Optional permanent setting)

~~~bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
~~~

## Clone the Repository

Clone the project to your local machine:

~~~bash
git clone https://github.com/LetsBeExplorers/ros2-robotics-tutorial.git
cd ros2-robotics-tutorial
~~~

This creates the project directory containing the ROS 2 workspace, configuration files, scripts, and documentation.

## Workspace Build

From the workspace root:

~~~bash
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
cd ..
~~~

## Launch Instructions

### Start Simulation

~~~bash
./start_sim.sh
~~~

This script:
- Cleans old Gazebo processes
- Launches TurtleBot3 world in Gazebo

### Start Autonomy Stack

Open a new terminal:

~~~bash
./run.sh
~~~

This script:
- Cleans old ROS processes
- Builds and sources the workspace
- Launches perception, behavior, and platform nodes
- Loads YAML configuration parameters

The robot will begin autonomous navigation.

## Reproducing the Demo

1. Source ROS 2:

   ~~~bash
   source /opt/ros/jazzy/setup.bash
   ~~~

2. Build the workspace:

   ~~~bash
   cd ros2_ws
   colcon build --symlink-install
   source install/setup.bash
   cd ..
   ~~~

3. Start the simulator:

   ~~~bash
   ./start_sim.sh
   ~~~

4. Launch the autonomy stack:

   ~~~bash
   ./run.sh
   ~~~

5. Observe autonomous robot behavior in Gazebo.

6. Inspect ROS communication:

   ~~~bash
   ros2 topic list
   ros2 topic echo /scan
   ros2 topic echo /cmd_vel
   rqt_graph
   ~~~

## Repository Structure

~~~
ros2-robotics-tutorial/
├── ros2_ws/
│   ├── src/
│   │   ├── perception/
│   │   ├── behavior/
│   │   └── platform_interface/
│   ├── build/        (ignored by git)
│   ├── install/      (ignored by git)
│   └── log/          (ignored by git)
│
├── config/
│   └── robot_params.yaml
│
├── docs/
│   ├── environment_setup.md
│   ├── tutorial_outline.md
│   ├── demo_steps.md
│   └── lessons_learned.md
│
├── start_sim.sh
├── run.sh
└── README.md
~~~

## Learning Outcomes

By completing this tutorial, learners will understand:

- ROS 2 node and topic communication
- Robot motion control using velocity commands
- Sensor-driven decision making
- Reactive obstacle avoidance design
- Modular robotics system architecture
- Simulation-based robotics development workflows
