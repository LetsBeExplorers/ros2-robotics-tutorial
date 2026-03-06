import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class PlatformInterface(Node):

    def __init__(self):
        super().__init__('platform_interface')

        # Receives high-level commands
        self.subscription = self.create_subscription(
            TwistStamped,
            '/robot_command',
            self.command_callback,
            10
        )

        # Sends commands to robot
        self.publisher = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

    def command_callback(self, msg):
        # For now, just forward the command
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PlatformInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()