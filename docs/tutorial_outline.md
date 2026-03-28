# ROS 2 Autonomous Navigation Tutorial – Flow Outline

## Introduction (0–5 min)

### Goals
- Introduce ROS 2 and its role in robotics
- Explain why simulation is used
- Set expectations for the tutorial

### Key Points
- ROS 2 as a modular robotics framework
- Simulation (Gazebo) enables safe testing
- Overview of what will be built:
  - Perception → decision → control pipeline
  - Reactive obstacle avoidance system

## Setup & System Overview (5–15 min)

### Goals
- Show development environment
- Explain project structure
- Launch the system

### Demo Flow
- Show OS, ROS 2 version, and simulator
- Walk through workspace structure (`ros2_ws/src`)
- Explain build process (`colcon build`)
- Run simulation and autonomy stack
- Verify robot appears and is running

### Concepts
- ROS 2 workspace and packages
- Build + source workflow
- Launch automation

## ROS 2 Core Concepts (15–25 min)

### Goals
- Explain how ROS systems communicate
- Demonstrate tools for inspecting the system

### Demo
- List active topics
- Echo sensor data
- Inspect velocity commands
- Visualize node graph

### Concepts
- Nodes = independent processes
- Topics = communication channels
- Publishers vs subscribers
- Key system topics:
  - `/scan` (sensor data)
  - `/cmd_vel` (motion commands)
  - `/odom`, `/tf` (state + transforms)

## System Architecture & Code (25–40 min)

### Goals
- Explain how the system is structured
- Walk through each major component

### Architecture Flow
- Sensor → Perception → Behavior → Robot

### Components

#### Perception
- Processes LiDAR data
- Divides environment into sectors
- Extracts obstacle distances

#### Behavior
- Reactive control loop
- Chooses direction based on obstacles
- Generates velocity commands

#### Platform Interface
- Converts commands into robot motion
- Abstracts hardware/simulator differences

### Key Concepts
- Modular system design
- Separation of responsibilities
- Real-time data flow between nodes

## Parameters and System Behavior (40–50 min)

### Goals
- Explain how the robot’s behavior is controlled and adjusted
- Connect system design → actual motion decisions

### Parameters
- Distance thresholds define safety zones
- Motion parameters
- LiDAR sector definitions

### System Implementation
- Perception node
- Behavior node
- Interface node

### What to Watch During the Demo
- Sensor data drives all decisions
- No map or path planning
- Obstacles trigger immediate responses
- Robot turns toward open space
- Turn commitment keeps motion stable

## Live Demonstration (50–55 min)

### Goals
- Show the system working in real time

### While Running
- Explain robot behavior live:
  - Why it turns
  - Why it slows/stops
- Connect sensor input → motion output
- Highlight continuous feedback loop

## Troubleshooting & Lessons (55–58 min)

### Common Issues
- Robot not moving → `/cmd_vel` not publishing
- Spinning → thresholds too sensitive
- Ignoring obstacles → `/scan` issue
- Erratic motion → tuning or sensor noise

### Lessons
- Modular design simplifies debugging
- Parameter tuning is critical
- ROS tools help diagnose issues quickly

## Recap & Closing (58–60 min)

### Summary
- Built a complete ROS 2 autonomy pipeline
- Connected perception, decision-making, and control
- Demonstrated real-time reactive navigation
- Showed modular node-based system design

### Resources
- Project repository (GitHub)
- ROS 2 documentation
- Gazebo simulator documentation
