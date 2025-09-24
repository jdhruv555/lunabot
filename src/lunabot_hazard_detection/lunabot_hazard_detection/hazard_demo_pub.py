import rclpy
from rclpy.node import Node
from vision_msgs.msg import Detection2DArray, Detection2D
from std_msgs.msg import Header

class HazardDemoPub(Node):
    def __init__(self):
        super().__init__(hazard_demo_pub)
        self.pub = self.create_publisher(Detection2DArray, hazards, 10)
        self.timer = self.create_timer(1.0, self.tick)

    def tick(self):
        msg = Detection2DArray()
        msg.header = Header()
        d = Detection2D()
        msg.detections.append(d)
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = HazardDemoPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
