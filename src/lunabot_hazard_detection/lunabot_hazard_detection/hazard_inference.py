import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

class HazardInference(Node):
    def __init__(self):
        super().__init__(hazard_inference)
        self.create_subscription(Image, camera/image_raw, self.cb, 10)
        self.pub = self.create_publisher(Detection2DArray, hazards, 10)

    def cb(self, msg: Image):
        # placeholder: publish empty detections
        self.pub.publish(Detection2DArray())


def main():
    rclpy.init()
    node = HazardInference()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
