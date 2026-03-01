# Environment Setup Guide

This document describes how to configure the development environment required to run the ROS 2 Autonomous Navigation Tutorial.

## 1. Operating System

- Ubuntu 24.04 LTS

Verify Ubuntu version:

~~~bash
lsb_release -a
~~~

## 2. Install ROS 2 Jazzy

Follow the official ROS 2 Jazzy installation guide for Ubuntu 24.04.

After installation, source ROS:

~~~bash
source /opt/ros/jazzy/setup.bash
~~~

To verify installation:

~~~bash
echo $ROS_DISTRO
~~~

Expected output:

~~~
jazzy
~~~

Optional verification:

~~~bash
ros2 doctor
~~~

## 3. Install Gazebo Harmonic

Verify Gazebo installation:

~~~bash
gz sim --versions
~~~

Expected output should display version 8.x.x (Harmonic).

If Gazebo is not installed:

~~~bash
sudo apt update
sudo apt install gz-sim
~~~

## 4. Install Required ROS 2 Packages

Install ROS–Gazebo integration packages:

~~~bash
sudo apt install ros-jazzy-gz-sim ros-jazzy-gz-ros2-control
~~~

(Additional dependencies will be listed here as development progresses.)

## 5. Create ROS 2 Workspace

Create a new workspace:

~~~bash
mkdir -p ~/ros2_tutorial_ws/src
cd ~/ros2_tutorial_ws
colcon build
~~~

## 6. Source Workspace

After building:

~~~bash
source install/setup.bash
~~~

To automatically source in new terminals (optional):

~~~bash
echo "source ~/ros2_tutorial_ws/install/setup.bash" >> ~/.bashrc
~~~

## 7. Verify ROS 2 and Gazebo Communication

(To be completed after robot integration is added.)