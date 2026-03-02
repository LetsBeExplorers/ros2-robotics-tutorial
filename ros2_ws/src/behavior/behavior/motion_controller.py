import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray

class MotionController(Node):

    def __init__(self):
        super().__init__('motion_controller')

        # Publisher for velocity commands
        self.publisher_ = self.create_publisher(
            Twist,
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
        msg = Twist()

        # Reactive obstacle avoidance logic
        if self.front > 0.6:
            # Path is clear → move forward
            msg.linear.x = 0.2
            msg.angular.z = 0.0
        else:
            # Obstacle ahead → turn toward open side
            msg.linear.x = 0.0
            if self.left > self.right:
                msg.angular.z = 0.6
            else:
                msg.angular.z = -0.6

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()