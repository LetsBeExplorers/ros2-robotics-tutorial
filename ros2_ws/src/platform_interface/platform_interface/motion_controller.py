import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped


class MotionController(Node):

    def __init__(self):
        super().__init__('motion_controller')

        # Publisher for velocity commands
        self.publisher_ = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

        # Run timer_callback every 0.1 seconds
        self.timer = self.create_timer(0.1, self.timer_callback)

        # Save start time so we can measure elapsed time
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]

    def timer_callback(self):
        # Create a new velocity message
        msg = TwistStamped()

        # Required frame for this setup
        msg.header.frame_id = 'base_link'

        # Calculate how long the node has been running
        current_time = self.get_clock().now().seconds_nanoseconds()[0]
        elapsed = current_time - self.start_time

        # Move forward for 5 seconds
        if elapsed < 5:
            msg.twist.linear.x = 0.2
            msg.twist.angular.z = 0.0

        # Rotate for the next 3 seconds
        elif elapsed < 8:
            msg.twist.linear.x = 0.0
            msg.twist.angular.z = 0.3

        # Stop after that
        else:
            msg.twist.linear.x = 0.0
            msg.twist.angular.z = 0.0

        # Send the command
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()