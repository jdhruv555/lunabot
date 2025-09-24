import rclpy
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped

def main():
    rclpy.init()
    node = rclpy.create_node('send_nav_goal')
    client = ActionClient(node, NavigateToPose, '/navigate_to_pose')
    if not client.wait_for_server(timeout_sec=30.0):
        node.get_logger().error('Nav2 action server not available')
        return
    goal = NavigateToPose.Goal()
    ps = PoseStamped()
    ps.header.frame_id = 'map'
    ps.pose.position.x = 1.5
    ps.pose.position.y = 0.0
    ps.pose.position.z = 0.0
    ps.pose.orientation.z = 0.0
    ps.pose.orientation.w = 1.0
    goal.pose = ps
    node.get_logger().info('Sending goal...')
    send_future = client.send_goal_async(goal)
    rclpy.spin_until_future_complete(node, send_future)
    goal_handle = send_future.result()
    if not goal_handle or not goal_handle.accepted:
        node.get_logger().error('Goal rejected')
        return
    result_future = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)
    node.get_logger().info('Navigation result: %r' % (result_future.result().result,))
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
