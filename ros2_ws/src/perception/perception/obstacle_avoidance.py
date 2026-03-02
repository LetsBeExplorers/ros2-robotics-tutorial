import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Create subscriber to /scan
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

    def scan_callback(self, msg):

        left_min = float('inf')
        front_min = float('inf')
        right_min = float('inf')

        for i, distance in enumerate(msg.ranges):
            if math.isinf(distance) or math.isnan(distance):
                continue

            angle = msg.angle_min + i * msg.angle_increment

            # Front sector: -30° to +30°
            if -math.radians(30) <= angle <= math.radians(30):
                front_min = min(front_min, distance)

            # Left sector: 30° to 90°
            elif math.radians(30) < angle <= math.radians(90):
                left_min = min(left_min, distance)

            # Right sector: -90° to -30°
            elif -math.radians(90) <= angle < -math.radians(30):
                right_min = min(right_min, distance)

        self.get_logger().info(
            f"L: {left_min:.2f} F: {front_min:.2f} R: {right_min:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()