import rclpy
from rclpy.node import Node
from vision_msgs.msg import Detection2DArray
from std_msgs.msg import String

class HazardAlertBridge(Node):
    def __init__(self):
        super().__init__(hazard_alert_bridge)
        self.sub = self.create_subscription(Detection2DArray, hazards, self.cb, 10)
        self.pub = self.create_publisher(String, alerts, 10)
        self.min_count = self.declare_parameter(min_count, 1).value

    def cb(self, msg: Detection2DArray):
        if len(msg.detections) >= self.min_count:
            alert = String()
            alert.data = f"Hazards detected: {len(msg.detections)}"
            self.pub.publish(alert)


def main():
    rclpy.init()
    node = HazardAlertBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
