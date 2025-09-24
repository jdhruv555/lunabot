from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path


def generate_launch_description():
    sim_pkg = get_package_share_path(lunabot_sim)
    desc_pkg = get_package_share_path(lunabot_description)

    world = LaunchConfiguration(world, default=str(sim_pkg / worlds / lunar_hab.world))

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(sim_pkg / launch / gazebo_bringup.launch.py),
        launch_arguments={world: world}.items()
    )

    spawn = Node(
        package=gazebo_ros, executable=spawn_entity.py, output=screen,
        arguments=[-entity, lunabot, -x, 0, -y, 0, -z, 0.1,
                   -topic, robot_description]
    )

    state_pub = Node(
        package=robot_state_publisher, executable=robot_state_publisher,
        parameters=[{robot_description: [xacro
