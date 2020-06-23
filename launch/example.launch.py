from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_pkg',
            executable='publisher',
            name='publisher',
            parameters=[
                {"frequency": 10.0},
                {"start_index": 100.0}
            ]
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