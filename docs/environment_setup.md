# Environment Setup Guide

This document describes how to configure the development environment required to run the ROS 2 Autonomous Navigation Tutorial.

## 1. Operating System

- Ubuntu 24.04 LTS

Verify Ubuntu version:

```bash
lsb_release -a
```

## 2. Install ROS 2 Jazzy

Follow the official ROS 2 Jazzy installation guide for Ubuntu 24.04.

After installation, source ROS:

```bash
source /opt/ros/jazzy/setup.bash
```

Verify installation:

```bash
echo $ROS_DISTRO
```

Expected output:

```
jazzy
```

Optional diagnostic check:

```bash
ros2 doctor
```

## 3. Install Gazebo Harmonic

Verify Gazebo installation:

```bash
gz sim --versions
```

Expected output should display version 8.x.x (Harmonic).

If Gazebo is not installed:

```bash
sudo apt update
sudo apt install gz-sim
```

## 4. Install Required ROS 2 Packages

Install ROS–Gazebo integration and TurtleBot3 packages:

```bash
sudo apt update
sudo apt install ros-jazzy-gz-sim ros-jazzy-gz-ros2-control ros-jazzy-ros-gz-bridge ros-jazzy-turtlebot3*
```

Verify installation:

```bash
ros2 pkg list | grep turtlebot3
```

You should see packages such as:

- turtlebot3_description  
- turtlebot3_gazebo  
- turtlebot3_bringup  

## 5. Set TurtleBot3 Model

The TurtleBot3 model must be defined before launching simulation.

For the Burger model:

```bash
export TURTLEBOT3_MODEL=burger
```

To make this permanent across new terminals:

```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

Verify:

```bash
echo $TURTLEBOT3_MODEL
```

Expected output:

```
burger
```

## 6. Launch Simulation

Start the official TurtleBot3 Gazebo world:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Wait until Gazebo fully loads and the TurtleBot3 robot appears in the world before proceeding.

## 7. If Simulation Fails to Start Cleanly

If Gazebo does not launch properly or the robot does not appear:

```bash
pkill -9 gz
pkill -9 ros2
```

Then open a new terminal and relaunch the simulation.

## 8. Build the ROS 2 Workspace

After cloning the repository, navigate to the workspace directory:

```bash
cd ros2_ws
colcon build
```

## 9. Source the Workspace

After building:

```bash
source install/setup.bash
```

To automatically source in new terminals (optional):

```bash
echo "source $(pwd)/install/setup.bash" >> ~/.bashrc
```

## 10. Verify ROS 2 and Gazebo Communication

After the robot appears, confirm active topics:

```bash
ros2 topic list
```

You should see topics such as:

- `/cmd_vel`
- `/odom`
- `/scan`
- `/tf`