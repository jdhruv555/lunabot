from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    pkg = get_package_share_path(lunabot_patrol)
    return LaunchDescription([
        Node(
            package=lunabot_patrol, executable=patrol_server, name=patrol_server,
            parameters=[{routes_file: str(pkg / config / patrol_routes.yaml), route_name: default, loop: True}],
        ),
    ])
