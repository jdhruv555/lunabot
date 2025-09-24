import math
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan

class DepthToScan(Node):
    def __init__(self):
        super().__init__(depth_to_scan)
        self.sub = self.create_subscription(Image, camera/depth/image_rect_raw, self.cb, 10)
        self.pub = self.create_publisher(LaserScan, scan_from_depth, 10)
        self.max_range = float(self.declare_parameter(max_range, 4.0).value)
        self.min_range = float(self.declare_parameter(min_range, 0.2).value)
        self.fov = float(self.declare_parameter(horizontal_fov, math.radians(70.0)).value)

    def cb(self, msg: Image):
        try:
            width = msg.width
            height = msg.height
            if width == 0 or height == 0:
                return
            # decode depth
            if msg.encoding == 32FC1:
                depth = np.frombuffer(msg.data, dtype=np.float32).reshape((height, width))
            elif msg.encoding == 16UC1:
                depth = np.frombuffer(msg.data, dtype=np.uint16).reshape((height, width)).astype(np.float32) / 1000.0
            else:
                return
            # use center row
            row = depth[height // 2]
            angles = np.linspace(-self.fov/2.0, self.fov/2.0, num=width, dtype=np.float32)
            ranges = np.clip(row, self.min_range, self.max_range)
            scan = LaserScan()
            scan.header = msg.header
            scan.angle_min = -self.fov/2.0
            scan.angle_max = self.fov/2.0
            scan.angle_increment = self.fov / float(width)
            scan.time_increment = 0.0
            scan.scan_time = 0.0
            scan.range_min = self.min_range
            scan.range_max = self.max_range
            scan.ranges = ranges.tolist()
            self.pub.publish(scan)
        except Exception:
            pass


def main():
    rclpy.init()
    node = DepthToScan()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
