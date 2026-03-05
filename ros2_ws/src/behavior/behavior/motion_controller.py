import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Float32MultiArray

class MotionController(Node):

    def __init__(self):
        super().__init__('motion_controller')

        # Publisher for velocity commands
        self.publisher_ = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

        # Store obstacle sector distances
        self.left = float('inf')
        self.front = float('inf')
        self.right = float('inf')

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
        self.left, self.front, self.right = msg.data

    def timer_callback(self):
        self.get_logger().info("Timer alive")
        msg = TwistStamped()

        danger = 0.2
        caution = 0.4

        if self.front < danger:
            self.get_logger().info("Danger Front!")

        elif self.front < caution:
            self.get_logger().info("Caution Front!")

        elif self.left < danger:
            self.get_logger().info("Danger Left!")

        elif self.left < caution:
            self.get_logger().info("Caution Left!")

        elif self.right < danger:
            self.get_logger().info("Danger Right!")

        elif self.right < caution:
            self.get_logger().info("Caution Right!")

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        msg.twist.linear.x = 0.2
        msg.twist.angular.z = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()