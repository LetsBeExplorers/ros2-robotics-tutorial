# Lesson Notes – Current Progress

These notes document important observations, gotchas, and lessons learned while working through the tutorial.

## 1. ROS 2 and Simulation

- ROS 2 handles communication between nodes.
- Gazebo handles physics simulation.

In this setup:
- Gazebo simulates the TurtleBot3 robot.
- ROS 2 sends commands and receives sensor data.

Key takeaway:
ROS and Gazebo are separate systems connected through topics.

## 2. Launching the Robot

Simulation was launched using:

```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

This:
- Starts Gazebo
- Spawns the TurtleBot3 model
- Starts controller and sensor plugins

Gotcha:
If `TURTLEBOT3_MODEL` is not set, the robot may not spawn.

## 3. Inspecting Topics

We used:

```
ros2 topic list
```

Important topics observed:

- `/cmd_vel`
- `/scan`
- `/odom`
- `/tf`

At this stage, `/cmd_vel` is the most important topic.

## 4. Understanding `/cmd_vel`

We checked:

```
ros2 topic info /cmd_vel
```

Output showed:
- Message type: `geometry_msgs/msg/TwistStamped`
- 1 subscriber (robot controller)

Gotcha:
Publishing `Twist` does NOT work.
The message type must match exactly.

## 5. Publishing Velocity Commands

To move forward:

```
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"
```

Notes:
- `-r 10` publishes at 10 Hz.
- The controller keeps applying the last received velocity.
- Stopping the publisher does NOT stop the robot.

## 6. Stopping the Robot

To stop:

```
ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"
```

Important lesson:
You must explicitly send zero velocity.

## 7. Simulation Reset Behavior

Pressing reset in Gazebo can remove the robot.

If that happens:
- Relaunch the simulation.

## 8. Environment Variables

TurtleBot3 requires:

```
TURTLEBOT3_MODEL=burger
```

If not set:
- Robot may not spawn.

Environment variables set with `export` only apply to the current terminal session.
Add to `~/.bashrc` to make permanent.

## 9. Custom Motion Controller Node

A Python node (`motion_controller.py`) was created to automate motion.

Important concepts learned:

- `super().__init__('motion_controller')` initializes the ROS node.
- `self.create_publisher()` registers a publisher.
- `self.create_timer()` runs a function at fixed intervals.
- `if __name__ == '__main__':` ensures `main()` runs only when executed directly.

Gotcha:
The node must be registered in `setup.py` using:

```
entry_points={
    'console_scripts': [
        'motion_controller = platform_interface.motion_controller:main',
    ],
}
```

Without this, `ros2 run` will not find the node.

After editing code:
- Run `colcon build`
- Then `source install/setup.bash`

## 10. Note on `/scan`

The `/scan` topic publishes LiDAR distance data (`sensor_msgs/msg/LaserScan`).

We have not used it yet.

It will be used later for obstacle detection.