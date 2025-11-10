import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimipleSubscriber(Node):
    def __init__(self): # constructor ran on creation of new object
        super().__init__("simple_subscriber")

        self.sub_ = self.create_subscription(String, "chatter", self.msgCallback, 10) # subscriber object with string input

    def msgCallback(self, msg):
        self.get_logger().info("I heard: %s " % msg.data)

def main():
    rclpy.init()
    simple_subscriber = SimipleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()