from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    use_sim_time = LaunchConfiguration(use_sim_time, default=false)
    pkg_path = get_package_share_path(lunabot_mapping)

    return LaunchDescription([
        DeclareLaunchArgument(use_sim_time, default_value=false),
        Node(
            package=cartographer_ros, executable=cartographer_node, name=cartographer,
            parameters=[{use_sim_time: use_sim_time}],
            arguments=[-configuration_directory, str(pkg_path / config),
                      -configuration_basename, cartographer.lua]
        ),
        Node(
            package=cartographer_ros, executable=cartographer_occupancy_grid_node, name=carto_grid,
            parameters=[{use_sim_time: use_sim_time}, {resolution: 0.05}],
        )
    ])
