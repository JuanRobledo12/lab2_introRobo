from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='team99_object_follower',
            namespace='find_ball',
            executable='detect_ball',
            name='detect'
        ),
        Node(
            package='team99_object_follower',
            namespace='rotate_robot',
            executable='rotate_turtle',
            name='rotate'
        )
    ])