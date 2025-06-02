import rclpy
from rclpy.node import Node
import subprocess

class UtilityNode(Node):
    def __init__(self):
        super().__init__('utility_node')
        self.timer = self.create_timer(5.0, self.check_status)

    def check_status(self):
        nodes = subprocess.getoutput("ros2 node list").splitlines()
        cpu_info = subprocess.getoutput("ros2 topic info /CPU")
        temp_info = subprocess.getoutput("ros2 topic info /temp")

        cpu_pubs = cpu_info.count('Publisher count')
        temp_pubs = temp_info.count('Publisher count')

        self.get_logger().info(f'Total Nodes: {len(nodes)}')
        self.get_logger().info(f'/CPU Publishers: {cpu_pubs}, /temp Publishers: {temp_pubs}')

def main(args=None):
    rclpy.init(args=args)
    node = UtilityNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

