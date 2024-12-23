import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class phoneNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.subscriber_ = self.create_subscription(String, "RoboNews", self.callbackFunc, 10)
        # syntax: create_publisher(type, "topicname", callbackFunc, buffer)
        self.get_logger().info("Smartphone has just begun listening...")
   
    def callbackFunc(self, mssge):
        self.get_logger().info(mssge.data)

def main(args=None):
    rclpy.init(args=args)

    node = phoneNode("robonews_listener_node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()