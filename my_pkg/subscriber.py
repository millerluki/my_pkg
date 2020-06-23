import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber_node')
        self.get_logger().info("Running...")
        self._a = None
        self._b = None
        self._sub_a = self.create_subscription(Float64, 'topic_a', self._cb_sub_a, 10)
        self._sub_b = self.create_subscription(Float64, 'topic_b', self._cb_sub_b, 10)
        self._sub_a  # prevent unused variable warning
        self._sub_b  # prevent unused variable warning

    def _cb_sub_a(self, msg):
        self._a = msg.data
        if (self._a and self._b is not None):
            self._c = self._a + self._b
            output = "{0} + {1} = {2}".format(self._a, self._b, self._c)
            self.get_logger().info(output)

    def _cb_sub_b(self, msg):
        self._b = msg.data


def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()