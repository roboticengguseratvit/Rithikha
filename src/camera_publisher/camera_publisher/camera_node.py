import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_node')

        # Publisher
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)

        # OpenCV camera capture (try device 0)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Failed to open camera.")
            return

        # CV Bridge
        self.br = CvBridge()

        # Timer for publishing frames
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to capture frame from camera")
            return

        # Show the frame
        cv2.imshow("Camera Feed", frame)
        cv2.waitKey(1)

        # Publish the image
        msg = self.br.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    rclpy.spin(node)

    # Cleanup
    node.cap.release()
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

