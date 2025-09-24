import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Int32

class DepthToObstacles(Node):
    def __init__(self):
        super().__init__(depth_to_obstacles)
        self.sub = self.create_subscription(Image, camera/depth/image_rect_raw, self.cb, 10)
        self.pub = self.create_publisher(Int32, depth/obstacle_count, 10)
        self.max_range = float(self.declare_parameter(max_range, 2.5).value)

    def cb(self, msg: Image):
        try:
            if msg.encoding not in (32FC1, 16UC1):
                return
            data = np.frombuffer(msg.data, dtype=np.float32 if msg.encoding==32FC1 else np.uint16)
            if msg.encoding == 16UC1:
                data = data.astype(np.float32) / 1000.0
            close = int(np.sum((data > 0.0) & (data < self.max_range)))
            out = Int32(); out.data = close
            self.pub.publish(out)
        except Exception:
            pass


def main():
    rclpy.init()
    node = DepthToObstacles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
