from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_path
from launch_ros.actions import Node


def generate_launch_description():
    desc_pkg = get_package_share_path(lunabot_description)
    display_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(desc_pkg / launch / display.launch.py)
    )

    base_node = Node(
        package=lunabot_base, executable=base_driver, name=base_driver,
        parameters=[{publish_tf: True, odom_frame: odom, base_frame: base_link}]
    )

    perception_pkg = get_package_share_path(lunabot_perception)
    # Directly start perception nodes
    lidar = Node(package=lunabot_perception, executable=lidar_filter, name=lidar_filter)
    depth = Node(package=lunabot_perception, executable=depth_to_obstacles, name=depth_to_obstacles)

    return LaunchDescription([
        display_launch,
        base_node,
        lidar,
        depth,
    ])
