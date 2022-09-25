#!/usr/bin/env phython

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalRotationControler(Node):

    def __init__(self):
        super().__init__('minimal_rotation_controler')
        self.pose_subscriber_ = self.create_subscription(Twist, '/turtlebot3/ball_pose', self.get_ball_coordinates, 10)
        self.get_logger().info("Rotation control node started!!")
        self.vel_publisher = self.create_publisher(Twist, '/cmd_vel', 5)

    def get_ball_coordinates(self, msg: Twist, center = 160, speed_gain = 2):
        self.vel_msg = Twist()
        #self.get_logger().info(str(msg.linear.x))
        ballpos_x = msg.linear.x 
        if (ballpos_x >= center-5) and (ballpos_x <= center+5):
            self.get_logger().info('the ball is already in the center')
            self.vel_msg.angular.z = 0.0
            self.vel_publisher.publish(self.vel_msg) 
        elif (ballpos_x < center-5) or ((ballpos_x > center+5) and (ballpos_x <= 320)):
            speed = speed_gain * -(ballpos_x-center) / center
            self.get_logger().info('rotating...')
            self.vel_msg.angular.z = speed
            self.vel_publisher.publish(self.vel_msg)
        elif (ballpos_x >= 10000.0):
            self.get_logger().info("I'm lost, please help me!")
            self.vel_msg.angular.z = 0.0
            self.vel_publisher.publish(self.vel_msg)
        


def main():
    rclpy.init()
    pose_sub = MinimalRotationControler()
    rclpy.spin(pose_sub)
    rclpy.shutdown()

if __name__ == '__main__':
	main()
