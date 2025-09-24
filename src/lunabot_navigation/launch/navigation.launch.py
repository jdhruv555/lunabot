from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    use_sim_time = LaunchConfiguration(use_sim_time, default=false)
    params_file = LaunchConfiguration(params_file)
    pkg_path = get_package_share_path(lunabot_navigation)

    return LaunchDescription([
        DeclareLaunchArgument(use_sim_time, default_value=false),
        DeclareLaunchArgument(params_file, default_value=str(pkg_path / config / nav2.yaml)),
        Node(
            package=nav2_controller, executable=controller_server, output=screen,
            parameters=[{use_sim_time: use_sim_time}, params_file]
        ),
        Node(
            package=nav2_planner, executable=planner_server, output=screen,
            parameters=[{use_sim_time: use_sim_time}, params_file]
        ),
        Node(
            package=nav2_bt_navigator, executable=bt_navigator, output=screen,
            parameters=[{use_sim_time: use_sim_time}, params_file]
        ),
        Node(
            package=nav2_recoveries, executable=recoveries_server, output=screen,
            parameters=[{use_sim_time: use_sim_time}, params_file]
        ),
        Node(
            package=nav2_lifecycle_manager, executable=lifecycle_manager, name=lifecycle_manager_navigation,
            output=screen, parameters=[{use_sim_time: use_sim_time}, {autostart: True},
                                         {node_names: [controller_server,planner_server,bt_navigator,recoveries_server]}]
        )
    ])
