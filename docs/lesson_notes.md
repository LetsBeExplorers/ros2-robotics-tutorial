# Lessons Learned While Building the ROS 2 Navigation System

These notes summarize important technical lessons, common mistakes, and useful insights discovered while developing the ROS 2 reactive obstacle avoidance system.

## 1. ROS 2 and Gazebo Work as Separate Systems

ROS 2 handles communication between nodes, while Gazebo handles the physics simulation.

- Gazebo simulates the TurtleBot3 robot and its sensors.
- ROS 2 sends motion commands and processes sensor data.

Lesson learned:  
Even though everything runs together, ROS and Gazebo are separate systems that communicate through topics.

## 2. Simulation Setup Depends on Environment Variables

Launching the TurtleBot3 simulation requires setting:

```
TURTLEBOT3_MODEL=burger
```

If this is missing, the robot may not spawn.

Lesson learned:  
Environment variables can control how simulations behave and are easy to forget.

Also, resetting Gazebo can remove the robot and break connections.

Lesson learned:  
Sometimes it’s faster to relaunch the simulation than to troubleshoot a broken reset.

## 3. ROS Topics Control Everything

ROS systems rely entirely on topics for communication between nodes.

Important topics observed:

- `/cmd_vel` — velocity commands
- `/scan` — LiDAR sensor data
- `/odom` — odometry
- `/tf` — coordinate transforms

Lesson learned:  
If something isn’t working, checking topics is one of the fastest ways to debug.

## 4. Message Types Must Match Exactly

The TurtleBot3 controller expects:

```
geometry_msgs/msg/TwistStamped
```

Publishing a `Twist` message does not work.

Lesson learned:  
ROS is strict about message types — even small mismatches prevent communication.

## 5. Robots Keep Moving Until Told to Stop

Stopping a velocity publisher does not stop the robot.

The robot keeps using the last command it received.

To stop it, a zero-velocity command must be sent.

Lesson learned:  
Robots must be explicitly told to stop.

## 6. Writing Custom ROS Nodes

Creating custom nodes helped clarify how ROS programs are structured.

Important concepts:

- `super().__init__()` initializes the node
- Publishers send messages
- Timers create control loops
- The `main()` function runs the node

### Node Registration

Nodes must be registered in `setup.py` as console scripts or ROS cannot run them.

After code changes:
- Rebuild with `colcon build`
- Re-source the workspace

Lesson learned:  
If ROS cannot find a node, it’s often a packaging or build issue.

## 7. Reactive Control Can Cause Jitter

Early obstacle avoidance caused the robot to rapidly switch directions when facing obstacles.

Cause:
- Decisions changed too quickly between control cycles.

Fix:
- Added turn commitment so the robot keeps turning briefly before reassessing.

Lesson learned:  
Reactive systems need stability, or they become noisy and unpredictable.

## 8. Hardcoded Values Make Tuning Difficult

Speeds and safety distances were originally hardcoded.

This made tuning behavior slow and required constant code edits.

Fix:
- Moved parameters to a YAML configuration file.

Lesson learned:  
Separating logic from tuning parameters makes systems easier to adjust.

## 9. ROS Parameters Only Work If Loaded Correctly

Parameters did not affect behavior when nodes were launched normally.

They only applied when launched with:

```
--ros-args --params-file
```

Lesson learned:  
ROS does not automatically load configuration files — they must be specified at launch.

## 10. Python Class Variables Need `self.`

A bug occurred when class variables were used without `self.`.

Incorrect:

```
linear = forward_speed
```

Correct:

```
linear = self.forward_speed
```

Lesson learned:  
Inside classes, variables must be referenced through the object instance.

## 11. Modular Packages Make Systems Cleaner

The project was split into:

- Perception package
- Behavior package
- Platform interface package

This initially made file organization confusing.

Lesson learned:  
Large ROS systems are easier to manage when separated by responsibility.

## 12. Old ROS Processes Can Cause Hidden Problems

A common issue occurred when previous ROS nodes were still running in the background.

Symptoms included:
- Duplicate topic publishers
- Robot behaving unpredictably
- Commands appearing to have no effect
- New nodes not launching properly

Cause:
- Old processes were not terminated before relaunching

Fix:
- Manually killed old nodes using `pkill`
- Added cleanup steps to launch scripts

Lesson learned:  
Leftover processes can silently interfere with new ROS sessions. Cleaning old nodes before relaunching prevents many confusing issues.

## 13. Conda Can Break ROS Builds

Conda environments override the system Python used by ROS.

This caused build failures until Conda was deactivated.

Fix:

```
conda deactivate
```

Lesson learned:  
ROS works best with the system Python environment.

## 14. Sensor Data Must Be Simplified Before Use

Raw LiDAR data is complex and noisy.

Dividing it into angular sectors made it easier to:

- Detect obstacles
- Decide turning direction

Lesson learned:  
Perception is about simplifying raw data into useful information for decisions.