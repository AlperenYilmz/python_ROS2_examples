import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("adder_client_node_without_oop")
    # HAS THE SAME SERVICE NAME AS SERVER CODE
    client = node.create_client(AddTwoInts, "AdderService")
    
    while not client.wait_for_service(2):
        node.get_logger().warn("Waiting for server...")
    
    reqObj = AddTwoInts.Request()

    while True:
        try:
            reqObj.a = int(input("a:"))
            break
        except ValueError:
            print("Invalid entry. Only integers")

    while True:
        try:
            reqObj.b = int(input("b:"))
            break
        except ValueError:
            print("Invalid entry. Only integers")

    
    future = client.call_async(reqObj)
    rclpy.spin_until_future_complete(node, future)

    try:
        response = future.result()
        node.get_logger().info(str(reqObj.a) + " + " + str(reqObj.b) + " = " + str(response.sum))
    except Exception as e:
        node.get_logger().error("Service call failed. %r" %(e,))


    response
    
    rclpy.shutdown()

if __name__== "__main__":
    main()