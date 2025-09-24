import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarFilter(Node):
    def __init__(self):
        super().__init__(lidar_filter)
        self.sub = self.create_subscription(LaserScan, scan, self.cb, 10)
        self.pub = self.create_publisher(LaserScan, scan/filtered, 10)

    def cb(self, msg: LaserScan):
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = LidarFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
