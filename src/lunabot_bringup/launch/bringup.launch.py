from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_path
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false', description='Use simulation time if true')

    desc_pkg = get_package_share_path('lunabot_description')
    display_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(desc_pkg / 'launch' / 'display.launch.py')
    )

    return LaunchDescription([
        declare_use_sim_time,
        display_launch,
    ])
