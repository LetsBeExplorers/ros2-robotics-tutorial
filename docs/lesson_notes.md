# Lesson Notes – Current Progress

These notes support the portions of the tutorial completed so far.

## 1. ROS 2 and Simulation

ROS 2 handles communication between different processes (nodes).

Gazebo handles physics and robot simulation.

In this setup:

- Gazebo simulates the TurtleBot3 robot.
- ROS 2 allows us to send velocity commands and read sensor data.

## 2. Launching the Robot

We launched the simulation using:

```
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

This:

- Starts Gazebo
- Spawns the TurtleBot3 model
- Starts the robot controller

## 3. Inspecting Topics

We used:

```
ros2 topic list
```

to see active topics.

Important topics observed:

- `/cmd_vel`
- `/scan`
- `/odom`
- `/tf`

## 4. Understanding `/cmd_vel`

We checked:

```
ros2 topic info /cmd_vel
```

Output showed:

- Message type: `geometry_msgs/msg/TwistStamped`
- 1 subscriber (the robot controller)

Important lesson:

The message type must match exactly when publishing.

Publishing `Twist` did not work because the subscriber expected `TwistStamped`.

## 5. Publishing Velocity Commands

To move the robot forward:

```
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}"
```

Key points:

- `-r 10` publishes at 10 Hz.
- Continuous publishing is required for sustained motion.
- Velocity commands represent instantaneous control inputs.

## 6. Stopping the Robot

When publishing stopped, the robot continued moving.

Reason:

The controller continued applying the last received velocity.

To stop the robot, we explicitly sent zero velocity:

```
ros2 topic pub --once /cmd_vel geometry_msgs/msg/TwistStamped "{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.0}, angular: {z: 0.0}}}"
```

Important lesson:

Stopping the publisher does not automatically stop the robot.

## 7. Simulation Reset Behavior

Pressing reset in Gazebo can remove the robot from the world.

If that happens, the simulation must be relaunched.

This is normal behavior when entities are spawned through launch files.