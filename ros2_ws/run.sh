#!/bin/bash

trap "echo 'Stopping nodes...'; kill 0" SIGINT

echo "Killing old ROS processes..."
pkill -f ros2 2>/dev/null

echo "Building workspace..."
colcon build --symlink-install

echo "Sourcing workspace..."
source install/setup.bash

echo "Starting nodes..."

ros2 run perception obstacle_processor &
ros2 run behavior motion_controller &

wait