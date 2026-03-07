import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Float32MultiArray

class MotionController(Node):

    def __init__(self):
        super().__init__('motion_controller')

        # Publisher for velocity commands
        self.publisher_ = self.create_publisher(
            TwistStamped,
            '/robot_command',
            10
        )

        # Store obstacle sector distances
        self.left = float('inf')
        self.front = float('inf')
        self.right = float('inf')
        self.front_left = float('inf')
        self.front_right = float('inf')

        self.turn_direction = 0  # remembers chosen turn direction

        # Subscribe to processed obstacle information
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/obstacle_info',
            self.obstacle_callback,
            10
        )

        # Run control loop at 10 Hz
        self.timer = self.create_timer(0.1, self.timer_callback)

    def obstacle_callback(self, msg):
        # Update sector distances
        (self.left,
         self.front,
         self.right,
         self.front_left,
         self.front_right) = msg.data

    def timer_callback(self):

        self.get_logger().info(
            f"L:{self.left:.2f} FL:{self.front_left:.2f} "
            f"F:{self.front:.2f} FR:{self.front_right:.2f} "
            f"R:{self.right:.2f}"
        )

        msg = TwistStamped()

        # Danger distance thresholds
        danger = 0.2
        side_danger = 0.15
        corner_danger = 0.25

        forward_speed = 0.25
        turn_speed = 0.8

        # Default: move forward
        linear = forward_speed
        angular = 0.0

        # Front left obstacle
        if self.front_left < corner_danger:
            self.get_logger().info("TURNING RIGHT — Front Left Danger")
            linear = 0.0 
            angular = -turn_speed   # turn right hard

        # Front right obstacle
        elif self.front_right < corner_danger:
            self.get_logger().info("TURNING RIGHT — Front Left Danger")
            linear = 0.0 
            angular = turn_speed    # turn left hard

        # Front obstacle
        elif self.front < danger:
            self.get_logger().info("FRONT DANGER")

            linear = 0.0

            # If not already turning, choose direction
            if self.turn_direction == 0:
                if self.left > self.right:
                    self.turn_direction = 1   # left
                else:
                    self.turn_direction = -1  # right

            angular = turn_speed * self.turn_direction

        # Left side obstacle
        elif self.left < side_danger:
            self.get_logger().info("LEFT SIDE DANGER")
            linear = 0.0 
            angular = -turn_speed * 0.5

        # Right side obstacle
        elif self.right < side_danger:
            self.get_logger().info("LEFT SIDE DANGER")
            linear = 0.0
            angular = turn_speed * 0.5
        else:
            self.get_logger().info("CLEAR — MOVING FORWARD")

        # Speeds actually set here after decision
        msg.twist.linear.x = linear
        msg.twist.angular.z = angular

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        # Reset turning memory once obstacle cleared
        if self.front > danger:
            self.turn_direction = 0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()