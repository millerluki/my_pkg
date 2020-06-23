import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class Publisher(Node):

    def __init__(self):
        super().__init__('timer_publisher')
        self.get_logger().info("Running...")
        self._publisher = self.create_publisher(Float64, 'topic_a', 10)
        self._timer_period = 1.0  # seconds
        self._timer = self.create_timer(self._timer_period, self._cb_timer)
        self._i = 0.0

    def _cb_timer(self):
        msg = Float64()
        msg.data = self._i
        self._publisher.publish(msg)
        self._i += self._timer_period


def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()