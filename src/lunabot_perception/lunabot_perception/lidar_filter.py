import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarFilter(Node):
    def __init__(self):
        super().__init__(lidar_filter)
        self.sub = self.create_subscription(LaserScan, scan, self.cb, 10)
        self.pub = self.create_publisher(LaserScan, scan/filtered, 10)
        self.range_min = float(self.declare_parameter(range_min, 0.12).value)
        self.range_max = float(self.declare_parameter(range_max, 12.0).value)
        self.smooth_window = int(self.declare_parameter(smooth_window, 3).value)

    def cb(self, msg: LaserScan):
        arr = np.array(msg.ranges, dtype=np.float32)
        arr = np.clip(arr, self.range_min, self.range_max)
        if self.smooth_window > 1:
            k = self.smooth_window
            pad = k//2
            padded = np.pad(arr, (pad, pad), mode=edge)
            kernel = np.ones(k, dtype=np.float32) / float(k)
            arr = np.convolve(padded, kernel, mode=valid)
        out = LaserScan()
        out = msg
        out.ranges = arr.tolist()
        self.pub.publish(out)


def main():
    rclpy.init()
    node = LidarFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
