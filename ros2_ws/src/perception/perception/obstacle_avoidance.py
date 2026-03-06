import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32MultiArray
import math

# Perception node: processes raw LiDAR data into left/front/right distances
class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Subscribe to LiDAR scan data
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        # Publish processed obstacle information
        self.publisher = self.create_publisher(
            Float32MultiArray,
            '/obstacle_info',
            10
        )

    def scan_callback(self, msg):

        # Initialize sector minimum distances
        left_min = float('inf')
        front_min = float('inf')
        right_min = float('inf')

        # Iterate through all LiDAR measurements
        for i, distance in enumerate(msg.ranges):

            # Skip invalid readings
            if math.isinf(distance) or math.isnan(distance):
                continue

            # Convert index to angle
            angle = msg.angle_min + i * msg.angle_increment

            # Front sector (-30° to 30°)
            if -math.radians(30) <= angle <= math.radians(30):
                front_min = min(front_min, distance)

            # Left sector (30° to 90°)
            elif math.radians(30) < angle <= math.radians(90):
                left_min = min(left_min, distance)

            # Right sector (-90° to -30°)
            elif -math.radians(90) <= angle < -math.radians(30):
                right_min = min(right_min, distance)

        # Publish sector distances
        msg_out = Float32MultiArray()
        msg_out.data = [left_min, front_min, right_min]
        self.publisher.publish(msg_out)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == "__main__":
    main()