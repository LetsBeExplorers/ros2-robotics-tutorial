# ROS 2 Autonomous Navigation Tutorial (Jazzy)

> Development in Progress

## Overview

This repository contains a ROS 2 tutorial project focused on demonstrating core robotics concepts using a simulated differential drive robot in Gazebo.

The goal of this project is to implement and demonstrate:

- ROS 2 workspace setup and build process  
- Node communication (publishers/subscribers)  
- Robot motion control  
- Sensor data interpretation  
- Reactive obstacle avoidance behavior  

The project is currently under active development.

## Planned System Configuration

- **Operating System:** Ubuntu 24.04 LTS  
- **ROS 2 Distribution:** Jazzy  
- **Simulation Environment:** Gazebo Harmonic  
- **Robot Type:** Differential drive mobile robot  
- **Primary Sensor:** LiDAR (LaserScan)  

## Current Status

- ROS 2 environment configured  
- Gazebo verified working  
- Project structure initialized  
- Robot integration and autonomous behavior in progress  

## Build Instructions

From inside the workspace root:

```bash
colcon build
source install/setup.bash
