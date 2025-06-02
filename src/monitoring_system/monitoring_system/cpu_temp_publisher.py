import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

class CPUTempPublisher(Node):
    def __init__(self):
        super().__init__('cpu_temp_publisher')
        self.cpu_pub = self.create_publisher(Float32, '/CPU', 10)
        self.temp_pub = self.create_publisher(Float32, '/temp', 10)
        self.timer = self.create_timer(5.0, self.publish_stats)

    def publish_stats(self):
        cpu_usage = psutil.cpu_percent(interval=1) / 50  # Normalize (0-2+)
        temps = psutil.sensors_temperatures()
        temp = temps.get('coretemp', [])[0].current if 'coretemp' in temps else 25.0
        self.cpu_pub.publish(Float32(data=cpu_usage))
        self.temp_pub.publish(Float32(data=temp))
        self.get_logger().info(f'Publishing CPU: {cpu_usage:.2f}, Temp: {temp:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = CPUTempPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

