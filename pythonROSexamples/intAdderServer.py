import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AdderServer(Node):
    def __init__(self):
        super().__init__("adder_server_node")
        self.server = self.create_service(AddTwoInts, "adder_service", self.serverCallback)
        self.get_logger().info("Adder service launched.")

    def serverCallback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response

def main(args = None):
    rclpy.init(args=args)
    node = AdderServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()