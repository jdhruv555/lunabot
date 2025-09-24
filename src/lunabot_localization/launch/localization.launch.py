from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration(use_sim_time, default=false)
    map_yaml = LaunchConfiguration(map, default=)

    return LaunchDescription([
        DeclareLaunchArgument(use_sim_time, default_value=false),
        DeclareLaunchArgument(map, default_value=),
        Node(
            package=nav2_map_server,
            executable=map_server,
            name=map_server,
            parameters=[{use_sim_time: use_sim_time}, {yaml_filename: map_yaml}]
        ),
        Node(
            package=nav2_amcl,
            executable=amcl,
            name=amcl,
            parameters=[{use_sim_time: use_sim_time},
                        {tf_broadcast: True},
                        config/amcl.yaml]
        ),
    ])
