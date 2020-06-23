from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_pkg',
            executable='publisher',
            name='publisher'
        ),
        Node(
            package='my_pkg',
            executable='transformer',
            name='transformer'
        ),
        Node(
            package='my_pkg',
            executable='subscriber',
            name='subscriber'
        )
    ])