from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package=lunabot_perception, executable=lidar_filter, name=lidar_filter),
        Node(package=lunabot_perception, executable=depth_to_obstacles, name=depth_to_obstacles),
        Node(package=lunabot_perception, executable=depth_to_scan, name=depth_to_scan),
    ])
