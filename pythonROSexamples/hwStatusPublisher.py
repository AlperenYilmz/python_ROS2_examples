import rclpy
from rclpy.node import Node
from custom_interfaces.msg import HardwareStat
# import name will be the same as the .msg filename

class statusPublisherNode(Node):
    def __init__(self):
        super().__init__("hardware_stat_publisher_node")
        self.publisherObj = self.create_publisher(HardwareStat, "hw_stat", 10)
        self.timerObj = self.create_timer(0.9, self.publisherCallback)
        self.get_logger().info("Hardware diagnostics running...")

    def publisherCallback(self):
        msgObj = HardwareStat()
        msgObj.motortemp = 70
        msgObj.is_motor_ready = True
        msgObj.debugmsg = "test"
        self.publisherObj.publish(msgObj)

def main(args=None):
    rclpy.init(args=args)
    node = statusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()