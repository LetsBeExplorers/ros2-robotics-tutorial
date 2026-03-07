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

        # Declare parameters and store their values
        self.danger = self.declare_parameter('danger', 0.2).value
        self.side_danger = self.declare_parameter('side_danger', 0.15).value
        self.corner_danger = self.declare_parameter('corner_danger', 0.25).value
        self.forward_speed = self.declare_parameter('forward_speed', 0.25).value
        self.turn_speed = self.declare_parameter('turn_speed', 0.8).value

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
        msg = TwistStamped()

        # Default: move forward
        linear = self.forward_speed
        angular = 0.0

        # Front left obstacle
        if self.front_left < self.corner_danger:
            linear = 0.0 
            angular = -self.turn_speed   # turn right hard

        # Front right obstacle
        elif self.front_right < self.corner_danger:
            linear = 0.0 
            angular = self.turn_speed    # turn left hard

        # Front obstacle
        elif self.front < self.danger:
            linear = 0.0

            # If not already turning, choose direction
            if self.turn_direction == 0:
                if self.left > self.right:
                    self.turn_direction = 1   # left
                else:
                    self.turn_direction = -1  # right

            angular = self.turn_speed * self.turn_direction

        # Left side obstacle
        elif self.left < self.side_danger:
            linear = 0.0 
            angular = -self.turn_speed * 0.5

        # Right side obstacle
        elif self.right < self.side_danger:
            linear = 0.0
            angular = self.turn_speed * 0.5

        # Speeds actually set here after decision
        msg.twist.linear.x = linear
        msg.twist.angular.z = angular

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        # Reset turning memory once obstacle cleared
        if self.front > self.danger:
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