from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    use_sim_time = LaunchConfiguration(use_sim_time, default=false)
    pkg_path = get_package_share_path(lunabot_state_estimation)

    return LaunchDescription([
        DeclareLaunchArgument(use_sim_time, default_value=false),
        Node(
            package=robot_localization,
            executable=ekf_node,
            name=ekf_filter_node,
            output=screen,
            parameters=[
                {use_sim_time: use_sim_time},
                str(pkg_path / config / ekf.yaml)
            ]
        )
    ])
