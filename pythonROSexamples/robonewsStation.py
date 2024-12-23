import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class robonewsPublisher(Node):
    def __init__(self):
        super().__init__()
        self.publisher_ = self.create_publisher(String, "RoboNews", 10)
        # syntax: create_publisher(type, "topicname", buffer)
        self.timer_ = self.create_timer(0.7, self.publisherFunc)
        self.get_logger().info("Robo News station is on AIR!")
   
    def publisherFunc(self):
        message = String()
        message.data = "Salam alaikum"
        self.publisher_.publish(message)

def main(args=None):
    rclpy.init(args=args)
    # initialize the rclpy with args passed to "main"

    node = robonewsPublisher("robonews_publisher_node")
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__=="__main__":
    main()