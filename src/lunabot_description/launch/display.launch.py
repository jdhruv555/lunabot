from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    pkg_path = get_package_share_path('lunabot_description')
    model_path = PathJoinSubstitution([str(pkg_path), 'urdf', 'lunabot.urdf.xacro'])

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false', description='Use simulation (Gazebo) clock if true')

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': Command(['xacro ', model_path])}]
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', str(pkg_path / 'launch' / 'display.rviz')],
        output='screen'
    )

    return LaunchDescription([
        declare_use_sim_time,
        robot_state_publisher,
        rviz,
    ])
