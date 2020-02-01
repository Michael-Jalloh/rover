from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python import get_package_share_directory

shr = get_package_share_directory("rover")
def generate_launch_description():
    print(shr)
    return LaunchDescription([
        Node(
            package="joy",
            node_executable="joy_node",
            #parameters=["./config.yml"]
            parameters=[os.path.join(shr, "config.yml")]
        ),
        Node(
            package="joy",
            node_executable="joy_node",
            #parameters=["./config.yml"]
            #parameters=[os.path.join(shr, "config.yml")]
        ),
        Node(
            package="rover",
            node_executable="controller",
            #parameters=["./config.yml"]
        ),
    ])