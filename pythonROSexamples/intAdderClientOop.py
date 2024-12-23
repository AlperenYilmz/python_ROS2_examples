import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class twoIntAdderNode(Node):
    aTemp = None    # defining temp values outside attributes
    bTemp = None
    def __init__(self):
        super().__init__("adder_client_node_oop")
        self.client_obj = self.create_client(AddTwoInts, "adder_service")
        
        while True:
            try:
                aTemp = int(input("a:"))
                break
            except ValueError:
                print("Invalid entry. Only integers")

        while True:
            try:
                bTemp = int(input("b:"))
                break
            except ValueError:
                print("Invalid entry. Only integers")
        self.get_logger().info("Parameters have been taken, requesting...")
        self.createRequest(aTemp, bTemp)

    def createRequest(self, a, b):
        while not self.client_obj.wait_for_service(3):
            self.get_logger().warn("Waiting for server...")
        
        request_obj = AddTwoInts.Request()   # creating request
        request_obj.a = a
        request_obj.b = b

        future_obj = self.client_obj.call_async(request_obj)   # passing request as future
        future_obj.add_done_callback(partial(self.futureHandler, a_pos=a, b_pos=b))
    
    # below callback will be executed when response acquired
    def futureHandler(self, future, a_pos, b_pos):
        try:
            response = future.result()
            self.get_logger().info(str(a_pos) + " + " + str(b_pos) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call has failed. %r" %(e,))

def main(args=None):
    rclpy.init(args=args)
    node = twoIntAdderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()