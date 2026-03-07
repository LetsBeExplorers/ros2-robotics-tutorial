# Tutorial Outline – ROS 2 Autonomous Navigation Workshop

This tutorial demonstrates a complete ROS 2 autonomy stack implementing reactive obstacle avoidance using TurtleBot3 in Gazebo simulation.

The workshop is structured to satisfy all required technical components through live demonstrations and code walkthroughs.

## 0–5 Minutes: Overview & Learning Goals

### Objectives
- Introduce ROS 2 and its role in robotics
- Explain simulation-based robot development
- Describe tutorial goals and outcomes

### Talking Points
- What is ROS 2?
- Why simulation before real robots?
- What is Gazebo?
- What is a differential drive robot?
- What students will learn:
  - ROS 2 environment setup
  - Workspace building
  - Node and topic communication
  - Sensor integration
  - Motion control
  - Reactive obstacle avoidance

## 5–15 Minutes: ROS 2 Setup & Launching Simulation

### Objectives
- Demonstrate ROS 2 environment
- Show workspace structure
- Build project using colcon
- Launch simulator and robot

### Live Demonstration
- Show OS and ROS 2 distribution
- Show workspace directory structure
- Explain build system
- Run simulation launch script
- Run autonomy stack script
- Verify robot appears in Gazebo

### Key Concepts
- ROS 2 workspace
- ROS 2 packages
- colcon build system
- Launch automation
- Simulation environments

## 15–25 Minutes: ROS 2 Core Concepts

### Objectives
- Demonstrate ROS 2 CLI tools
- Show node communication
- Visualize system architecture

### Live Demonstration
- List active topics
- Echo live sensor data
- Inspect velocity commands
- Display ROS graph visualization

### Concepts Explained
- Nodes
- Topics
- Publishers vs Subscribers
- Message types
- Modular robotics architecture

## 25–40 Minutes: Code Walkthrough

### Objectives
- Explain structure of custom ROS 2 nodes
- Demonstrate perception → decision → actuation pipeline
- Show meaningful custom node development

### Perception Node
- LaserScan subscriber
- Angular sector processing
- Obstacle distance extraction
- Publishing processed environment data

### Behavior Node
- Reactive control loop
- Obstacle avoidance decision logic
- Direction selection
- Motion command generation
- Parameterized behavior tuning

### Platform Interface Node
- Command forwarding
- Hardware abstraction
- Separation of autonomy and platform control

### Key Concepts
- Reactive vs deliberative robotics
- Control loop timing
- Safety thresholds
- Modular system design
- Parameterized configuration

## 40–55 Minutes: Autonomous Behavior Demonstration

### Objectives
- Demonstrate reactive obstacle avoidance
- Show robot motion control in simulation
- Use live sensor data for decision-making

### Live Demonstration
- Robot moves autonomously
- Robot avoids walls
- Robot navigates around obstacles
- Robot adapts continuously to environment

### Real-Time Explanations
- How LiDAR data is interpreted
- How control commands are generated
- Why robot turns and slows
- Interaction of linear and angular velocity
- Reactive behavior without path planning

## 55–60 Minutes: Troubleshooting & Recap

### Common Issues
- Environment not sourced
- Workspace build errors
- Missing topics
- Simulator launch failures
- DDS middleware conflicts
- Incorrect parameter tuning

### Recap
- ROS 2 setup and environment
- Core ROS communication concepts
- Sensor data integration
- Motion control interfaces
- Reactive obstacle avoidance
- Modular autonomy architecture

### Closing
- Encourage experimentation
- Suggest project extensions:
  - Wall following
  - Navigation stack (Nav2)
  - Mapping and SLAM
  - Multi-robot systems