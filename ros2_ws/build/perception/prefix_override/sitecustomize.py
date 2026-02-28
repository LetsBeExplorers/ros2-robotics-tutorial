import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/raytracer/projects/DASE4460/ros2-uav-demo/ros2_ws/install/perception'
