import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class Transformer(Node):

    def __init__(self):
        super().__init__('timer_publisher')
        self.get_logger().info("Running...")
        self._subscription = self.create_subscription(Float64, 'topic_a', self._cb_sub, 10)
        self._publisher = self.create_publisher(Float64, 'topic_b', 10)

    def _cb_sub(self, msg):
        # self.get_logger().info("Message received...")
        doubler = Float64()
        doubler.data = msg.data * 2
        self._publisher.publish(doubler)


def main(args=None):
    rclpy.init(args=args)
    transformer = Transformer()
    rclpy.spin(transformer)
    transformer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()