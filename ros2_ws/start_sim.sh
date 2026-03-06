#!/bin/bash

echo "Cleaning old simulator processes..."

# Kill Gazebo simulator engines
pkill -9 -f "gz sim" 2>/dev/null
pkill -9 -f gazebo 2>/dev/null

# Kill simulator bridges & robot model nodes
pkill -9 -f ros_gz_bridge 2>/dev/null
pkill -9 -f robot_state_publisher 2>/dev/null

# Kill old ros2 launch wrappers
pkill -9 -f "ros2 launch turtlebot3_gazebo" 2>/dev/null

# Kill stuck DDS middleware (safe)
pkill -9 -f fastdds 2>/dev/null
pkill -9 -f cyclonedds 2>/dev/null

sleep 1

echo "Starting Gazebo..."
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py