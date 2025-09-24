from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_path
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration(use_sim_time, default=false)

    desc_pkg = get_package_share_path(lunabot_description)
    base_node = Node(
        package=lunabot_base, executable=base_driver, name=base_driver,
        parameters=[{publish_tf: True, odom_frame: odom, base_frame: base_link}]
    )

    state_estimation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_package_share_path(lunabot_state_estimation) / launch / state_estimation.launch.py),
        launch_arguments={use_sim_time: use_sim_time}.items()
    )

    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_package_share_path(lunabot_localization) / launch / localization.launch.py),
        launch_arguments={use_sim_time: use_sim_time, map: }.items()
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_package_share_path(lunabot_navigation) / launch / navigation.launch.py),
        launch_arguments={use_sim_time: use_sim_time}.items()
    )

    perception = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_package_share_path(lunabot_perception) / launch / perception.launch.py)
    )

    display = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(desc_pkg / launch / display.launch.py)
    )

    return LaunchDescription([
        DeclareLaunchArgument(use_sim_time, default_value=false),
        display,
        base_node,
        state_estimation,
        localization,
        navigation,
        perception,
    ])
