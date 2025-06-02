import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CPUMonitor(Node):
    def __init__(self):
        super().__init__('cpu_temp_monitor')
        self.cpu_sub = self.create_subscription(Float32, '/CPU', self.cpu_callback, 10)
        self.temp_sub = self.create_subscription(Float32, '/temp', self.temp_callback, 10)

    def cpu_callback(self, msg):
        val = msg.data
        if val > 2.0:
            self.get_logger().fatal('Critical CPU USAGE')
            rclpy.shutdown()
        elif val >= 1.0:
            self.get_logger().info('Normal CPU USAGE')
        elif val >= 0.5:
            self.get_logger().warn('LOW CPU USAGE')

    def temp_callback(self, msg):
        val = msg.data
        if val > 60:
            self.get_logger().fatal('Time to buy a new Pi')
            rclpy.shutdown()
        elif val >= 20:
            self.get_logger().info('Normal Temperature')
        else:
            self.get_logger().warn('Low Temperature')

def main(args=None):
    rclpy.init(args=args)
    node = CPUMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

