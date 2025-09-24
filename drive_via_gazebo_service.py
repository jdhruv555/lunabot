import math, time
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
from geometry_msgs.msg import Pose, Point, Quaternion

MODEL_CANDIDATES = ["lunabot", "robot", "mobile_base", "model"]
STEP = 0.2   # meters per step
YAW = 0.0
SLEEP = 0.3  # seconds
STEPS = 40   # total steps forward

def q_from_yaw(y):
    return Quaternion(x=0.0, y=0.0, z=math.sin(y/2.0), w=math.cos(y/2.0))

def main():
    rclpy.init()
    node = rclpy.create_node("drive_via_gazebo_service")
    cli = node.create_client(SetEntityState, "/gazebo/set_entity_state")
    node.get_logger().info("Waiting for /gazebo/set_entity_state...")
    if not cli.wait_for_service(timeout_sec=15.0):
        node.get_logger().error("Service not available"); return
    # Try candidate model names until one works
    for name in MODEL_CANDIDATES:
        x = 0.0
        ok = False
        for i in range(STEPS):
            req = SetEntityState.Request()
            req.state = EntityState()
            req.state.name = name
            req.state.pose = Pose()
            x += STEP
            req.state.pose.position = Point(x=x, y=0.0, z=0.05)
            req.state.pose.orientation = q_from_yaw(YAW)
            fut = cli.call_async(req)
            rclpy.spin_until_future_complete(node, fut, timeout_sec=3.0)
            if fut.result() is None or (hasattr(fut.result(), "success") and not fut.result().success):
                ok = False
                break
            ok = True
            time.sleep(SLEEP)
        if ok:
            node.get_logger().info(f"Moved model {name} forward successfully.")
            break
        else:
            node.get_logger().info(f"Model {name} not found or cannot move; trying next...")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
