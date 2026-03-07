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

        # Declare perception parameters (degrees)
        self.front_angle = math.radians(self.declare_parameter('front_angle_deg', 45.0).value)
        self.corner_angle = math.radians(self.declare_parameter('corner_angle_deg', 70.0).value)
        self.side_angle = math.radians(self.declare_parameter('side_angle_deg', 120.0).value)

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
        front_left_min = float('inf')
        front_right_min = float('inf')

        # Iterate through all LiDAR measurements
        for i, distance in enumerate(msg.ranges):

            # Skip invalid readings
            if math.isinf(distance) or math.isnan(distance):
                continue

            # Convert index to angle
            angle = msg.angle_min + i * msg.angle_increment

            # Normalize angle to -π → +π
            if angle > math.pi:
                angle -= 2 * math.pi

            # Front-left corner
            if self.front_angle < angle <= self.corner_angle:
                front_left_min = min(front_left_min, distance)
                left_min = min(left_min, distance)

            # Front-right corner
            elif -self.corner_angle <= angle < -self.front_angle:
                front_right_min = min(front_right_min, distance)
                right_min = min(right_min, distance)

            # Front sector
            elif -self.front_angle <= angle <= self.front_angle:
                front_min = min(front_min, distance)

            # Left sector
            elif self.corner_angle < angle <= self.side_angle:
                left_min = min(left_min, distance)

            # Right sector
            elif -self.side_angle <= angle < -self.corner_angle:
                right_min = min(right_min, distance)

        # Publish sector distances
        msg_out = Float32MultiArray()
        msg_out.data = [left_min, front_min, right_min, front_left_min, front_right_min]
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