from launch import LaunchDescription
import launch_ros.actions 


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='hello_world', node_executable='talker',
            output='screen'),
        launch_ros.actions.Node(
            package='hello_world', node_executable='listener',
            output='screen'),
    ])
