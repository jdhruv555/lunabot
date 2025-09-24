import time, rclpy
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
def main():
    rclpy.init()
    node = rclpy.create_node("send_nav_goal_once")
    client = ActionClient(node, NavigateToPose, "/navigate_to_pose")
    node.get_logger().info("Waiting for Nav2 action server...")
    if not client.wait_for_server(timeout_sec=60.0):
        node.get_logger().error("Nav2 action server not available"); return
    goal = NavigateToPose.Goal()
    ps = PoseStamped(); ps.header.frame_id = "map"
    ps.pose.position.x = 1.5; ps.pose.position.y = 0.0
    ps.pose.orientation.z = 0.0; ps.pose.orientation.w = 1.0
    goal.pose = ps
    node.get_logger().info("Sending goal...")
    f = client.send_goal_async(goal); rclpy.spin_until_future_complete(node, f)
    gh = f.result()
    if not gh or not gh.accepted:
        node.get_logger().error("Goal rejected"); return
    rf = gh.get_result_async(); rclpy.spin_until_future_complete(node, rf)
    node.get_logger().info("Goal result received"); node.destroy_node(); rclpy.shutdown()
if __name__ == "__main__": time.sleep(8); main()
