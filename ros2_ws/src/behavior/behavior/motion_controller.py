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
        msg = TwistStamped()

        danger = 0.25
        forward_speed = 0.25
        turn_speed = 0.8

        # Default: move forward
        linear = forward_speed
        angular = 0.0

        if self.front < danger:
            # Turn toward clearer side
            linear = 0.0
            if self.left > self.right:
                angular = turn_speed
            else:
                angular = -turn_speed

        elif self.left < danger:
            linear = 0.1
            angular = -turn_speed * 0.5

        elif self.right < danger:
            linear = 0.1
            angular = turn_speed * 0.5

        msg.twist.linear.x = linear
        msg.twist.angular.z = angular

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

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