import rclpy
from rclpy.node import Node
import time
from sensor_msgs.msg import Joy
from rover.joystick import JoyStick
from rover.py import Py, findArduinoPort
from rover.motor import Motor
from rover.driver import Driver_2M

class Controller(Node):

    def __init__(self):
        super().__init__("controller_node")
        self.subscription = self.create_subscription( Joy, "joy", self.listener_callback, 10)
        self.subscription
        self.joystick = JoyStick()
        self.last_received = time.time()
        self.timeout = 2
        self.timer = self.create_timer(0.5, self.run)
        lmotor = Motor("left")
        rmotor = Motor("right")

        d = findArduinoPort()
        if d == None:
            exit()
        py = Py(d)
        self.rover = Driver_2M(lmotor, rmotor,py)

    def listener_callback(self, msg):
        self.joystick.update(msg)
        #self.get_logger().info(str(msg.buttons))
        self.last_received = time.time()
    
    def run(self):
        if time.time() - self.last_received <= self.timeout:
            #self.get_logger().info(str(self.joystick))
            if (self.joystick.r2 == -1):
                deadman_switch = True
                self.rover.set_speed(200)
                self.rover.stop_motor()
            else:
                deadman_switch = False
                self.rover.stop_motor()
            if(self.joystick.dup == 1 and deadman_switch == True):
                self.rover.forward()
            elif (self.joystick.ddown == 1 and deadman_switch == True):
                self.rover.backward()
            elif (self.joystick.dleft == 1 and deadman_switch == True):
                self.rover.turn_left()
            elif(self.joystick.dright == 1 and deadman_switch == True):
                self.rover.turn_right()
            else:
                self.rover.stop_motor()
        else:
            self.get_logger().info("Lost Connection")
            self.rover.stop_motor()

def main(args=None):
    rclpy.init(args=args)
    controller_node = Controller()

    rclpy.spin(controller_node)

    controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()