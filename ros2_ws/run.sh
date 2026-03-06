#!/bin/bash

stop_robot() {
    echo "Stopping robot motion..."

    timeout 2 ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped \
    "{twist: {linear: {x: 0.0}, angular: {z: 0.0}}}" 2>/dev/null

    echo "Stopping nodes..."
    pkill -f motion_controller
    pkill -f obstacle_avoidance
    pkill -f platform_interface
}

trap stop_robot SIGINT

echo "Cleaning old nodes..."

# Kill old nodes
pkill -f motion_controller 2>/dev/null
pkill -f obstacle_avoidance 2>/dev/null
pkill -f platform_interface 2>/dev/null

# Kill stuck ros2 CLI runs
pkill -f "ros2 run perception" 2>/dev/null
pkill -f "ros2 run behavior" 2>/dev/null
pkill -f "ros2 run platform_interface" 2>/dev/null

# Kill DDS middleware (safe for Gazebo)
pkill -f fastdds 2>/dev/null
pkill -f cyclonedds 2>/dev/null

sleep 1

echo "Building workspace..."
colcon build --symlink-install

echo "Sourcing workspace..."
source install/setup.bash

sleep 4

echo "Starting nodes..."
ros2 run platform_interface platform_interface &
ros2 run perception obstacle_avoidance &
ros2 run behavior motion_controller &


wait