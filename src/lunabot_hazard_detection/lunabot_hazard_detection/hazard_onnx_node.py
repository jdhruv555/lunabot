import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

class HazardOnnxNode(Node):
    def __init__(self):
        super().__init__(hazard_onnx_node)
        self.model_path = self.declare_parameter(model, ).value
        self.threshold = float(self.declare_parameter(threshold, 0.5).value)
        self.pub = self.create_publisher(Detection2DArray, hazards, 10)
        self.create_subscription(Image, camera/image_raw, self.cb, 10)
        self.session = None
        try:
            if self.model_path:
                import onnxruntime as ort  # type: ignore
                self.session = ort.InferenceSession(self.model_path)
                self.get_logger().info(fONNX
