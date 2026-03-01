# Tutorial Outline – ROS 2 Autonomous Navigation Workshop

This document structures the 60-minute recorded tutorial for the Intelligent Robotics assignment.

---

## 0–5 Minutes: Overview & Learning Goals

### Objectives
- Introduce ROS 2 and its role in modern robotics
- Explain what will be demonstrated
- Set expectations for the session

### Talking Points
- What is ROS 2?
- Why use simulation before real robots?
- What is Gazebo?
- What is a differential drive robot?
- What students will learn by the end:
  - Creating a workspace
  - Running a robot in simulation
  - Understanding topics and nodes
  - Writing a ROS 2 node
  - Implementing autonomous obstacle avoidance

---

## 5–15 Minutes: Setup & Launching Simulation

### Objectives
- Show workspace structure
- Build the project
- Launch Gazebo
- Spawn robot

### Live Demonstration
- Source ROS 2
- Build workspace using `colcon`
- Launch Gazebo simulation
- Verify robot appears
- Show `/cmd_vel` topic exists

### Key Concepts to Explain
- What is a workspace?
- What is a package?
- What does `colcon build` do?
- What is a launch file?

---

## 15–25 Minutes: ROS 2 Fundamentals

### Objectives
- Demonstrate core ROS 2 CLI tools
- Visualize system architecture

### Live Demonstration
- `ros2 topic list`
- `ros2 topic echo /scan`
- `ros2 topic info /cmd_vel`
- `rqt_graph`

### Concepts to Explain
- Nodes
- Topics
- Publishers vs Subscribers
- Message types (`geometry_msgs/Twist`, `sensor_msgs/LaserScan`)
- How ROS enables modular robotics

---

## 25–40 Minutes: Code Walkthrough

### Objectives
- Explain structure of custom ROS 2 node
- Show perception → decision → actuation flow

### Walkthrough Sections
1. Node initialization
2. Subscriber setup (LaserScan)
3. Publisher setup (`cmd_vel`)
4. Callback function logic
5. Obstacle detection threshold
6. Velocity command generation

### Key Concepts
- Reactive control vs planning
- Control frequency
- Safety considerations
- Why modular design matters

---

## 40–55 Minutes: Autonomous Behavior Demo

### Objectives
- Demonstrate robot navigating autonomously
- Show obstacle avoidance in action

### Live Demonstration
- Launch simulation
- Run autonomous node
- Show robot avoiding obstacles
- Use `ros2 topic echo` to observe live sensor data

### Explain in Real Time
- How LaserScan data is interpreted
- Why robot turns when obstacle detected
- How linear and angular velocity interact

---

## 55–60 Minutes: Troubleshooting & Recap

### Common Issues to Discuss
- Forgetting to source workspace
- Build errors
- Topics not appearing
- Gazebo not launching
- Dependency issues

### Recap
- What was built
- What ROS 2 concepts were demonstrated
- How to extend this project:
  - Wall following
  - Navigation stack (Nav2)
  - Multi-robot systems
  - Mapping and SLAM

### Closing Statement
- Reinforce understanding of ROS 2 architecture
- Encourage experimentation and extension