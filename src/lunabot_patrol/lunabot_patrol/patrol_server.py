import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
import yaml
from pathlib import Path
import math

class PatrolServer(Node):
    def __init__(self):
        super().__init__(patrol_server)
        self.declare_parameter(routes_file, )
        self.declare_parameter(route_name, default)
        self.declare_parameter(loop, True)

        routes_file = self.get_parameter(routes_file).value
        route_name = self.get_parameter(route_name).value
        self.loop = bool(self.get_parameter(loop).value)

        self.waypoints = []
        if routes_file:
            try:
                data = yaml.safe_load(Path(routes_file).read_text())
                self.waypoints = data.get(routes, {}).get(route_name, [])
            except Exception as exc:
                self.get_logger().error(f"Failed to load routes: {exc}")

        self.client = ActionClient(self, NavigateToPose, navigate_to_pose)
        self.index = 0
        self.in_flight = False
        self.timer = self.create_timer(0.5, self._tick)

    def _tick(self):
        if not self.waypoints or self.in_flight or not self.client.server_is_ready():
            return
        wp = self.waypoints[self.index]
        pose = PoseStamped()
        pose.header.frame_id = map
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = float(wp.get(x, 0.0))
        pose.pose.position.y = float(wp.get(y, 0.0))
        yaw = float(wp.get(yaw, 0.0))
        pose.pose.orientation.z = math.sin(yaw/2.0)
        pose.pose.orientation.w = math.cos(yaw/2.0)

        goal = NavigateToPose.Goal()
        goal.pose = pose
        self.in_flight = True
        future = self.client.send_goal_async(goal)
        future.add_done_callback(self._goal_response)

    def _goal_response(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.in_flight = False
            self._advance()
            return
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_cb)

    def _result_cb(self, future):
        self.in_flight = False
        self._advance()

    def _advance(self):
        self.index += 1
        if self.index >= len(self.waypoints):
            if self.loop:
                self.index = 0
            else:
                self.waypoints = []


def main():
    rclpy.init()
    node = PatrolServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
