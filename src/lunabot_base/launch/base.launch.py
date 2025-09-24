from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lunabot_base',
            executable='base_driver',
            name='base_driver',
            parameters=[{
                'publish_tf': True,
                'odom_frame': 'odom',
                'base_frame': 'base_link',
                'odom_publish_rate': 50.0,
            }]
        ),
    ])
