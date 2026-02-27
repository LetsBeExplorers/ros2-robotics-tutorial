# Autonomous UAV Simulation with ROS 2 (Jazzy)

> Work in Progress – Under Active Development

## Overview

This project demonstrates core ROS 2 concepts using a simulated UAV in Gazebo.  
It is being developed as part of an Intelligent Robotics tutorial assignment.

The tutorial will include:

- ROS 2 workspace setup and build (colcon)
- Node communication (publishers and subscribers)
- Robot motion control via ROS topics
- Sensor data interpretation
- Implementation of autonomous UAV behavior
- Use of ROS tools (ros2 topic, rqt_graph, etc.)

## System Configuration

- Operating System: Ubuntu 24.04 LTS  
- ROS 2 Distribution: Jazzy  
- Simulation Environment: Gazebo (to be finalized)

## Build Instructions

From inside `ros2_ws`:

```bash
colcon build
source install/setup.bash
