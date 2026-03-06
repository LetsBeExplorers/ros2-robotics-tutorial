#!/bin/bash

stop_robot() {
    echo "Stopping robot..."

    ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped \
    "{twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"

    echo "Stopping nodes..."
    kill 0
}

trap stop_robot SIGINT

echo "Killing old ROS & Gazebo processes..."
pkill -9 -f ros
pkill -9 -f gz

echo "Building workspace..."
colcon build --symlink-install

echo "Sourcing workspace..."
source install/setup.bash

echo "Starting nodes..."

ros2 run perception obstacle_avoidance &
ros2 run behavior motion_controller &

wait