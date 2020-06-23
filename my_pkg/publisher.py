import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class Publisher(Node):

    def __init__(self):
        super().__init__('timer_publisher')
        self.get_logger().info("Running...")

        self.declare_parameter("frequency", 0.5)
        self.declare_parameter("start_index", 0.0)

        self._publisher = self.create_publisher(Float64, 'topic_a', 10)

        frequency = self.get_parameter("frequency").get_parameter_value().double_value
        self._timer_period = 1/frequency
        self._timer = self.create_timer(self._timer_period, self._cb_timer)

        self._i= self.get_parameter("start_index").get_parameter_value().double_value

    def _cb_timer(self):
        msg = Float64()
        msg.data = float(self._i)
        self._publisher.publish(msg)
        self._i = self._i + 1


def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()