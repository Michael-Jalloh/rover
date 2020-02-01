import time

class Driver_2M(object):
    def __init__(self, leftMotor, rightMotor, com):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.com = com # com is the py instance used to communicate with the arduino
        self.speed = 0
        self.description = "This is a rover driver for a rover base with two motors left and right"

    def send_cmd(self, cmd, data):
        data = f"{cmd}/{data}"
        #print(data)
        self.com.write(data)
    
    def get_data(self, cmd):
        data = f"cmd/{cmd}"
        self.com.write(data)
        time.sleep(0.2)
        return self.com.get_data()

    def set_speed(self, speed):
        self.speed = speed
        self.leftMotor.set_speed(speed)
        self.rightMotor.set_speed(speed)
        data = f"{self.leftMotor.get_data()}&{self.rightMotor.get_data()}"
        self.send_cmd("speed", data)

    def set_motor_speed(self, speed, leftMotor = False, rightMotor = False):
        if(leftMotor):
            self.leftMotor.set_speed(speed)
        if(rightMotor):
            self.rightMotor.set_speed(speed)
        data = f"{self.leftMotor.get_data()}&{self.rightMotor.get_data()}"
        self.send_cmd("speed", data)

    def stop_motor(self, leftMotor = True, rightMotor = True):
        if(leftMotor):
            self.leftMotor.stop()
            print(leftMotor)
        if(rightMotor):
            self.rightMotor.stop()
            print(rightMotor)
        data = f"{self.leftMotor.get_data()}&{self.rightMotor.get_data()}"
        print(data)
        self.send_cmd("speed", data)

    def turn_right(self):
        speed = self.speed
        #if speed > 100:
        #    speed = 100
        self.set_speed(speed)
        self.leftMotor.forward()
        #self.rightMotor.backward()
        self.stop_motor(leftMotor=False)

    def turn_left(self):
        speed = self.speed
        #if speed > 100:
         #   speed = 100        
        self.set_speed(speed)
        self.rightMotor.forward()
        #self.leftMotor.backward()
        self.stop_motor(rightMotor=False)
    
    def turn_right_backwards(self):
        speed = self.speed
        if speed > 100:
            speed = 100
        self.leftMotor.backward()
        self.set_speed(speed)
        self.stop_motor(leftMotor=False)
    
    def turn_left_backwards(self):
        speed = self.speed
        if speed > 100:
            speed = 100
        self.rightMotor.backward()
        self.set_speed(speed)
        self.stop_motor(rightMotor=False)
    
    def forward(self):
        self.leftMotor.forward()
        self.rightMotor.forward()
        self.set_speed(self.speed)

    def backward(self):
        self.leftMotor.backward()
        self.rightMotor.backward()
        self.set_speed(self.speed)


    def shutdown(self):
        self.stop_motor(True, True)
        self.com.close()
        print("ShutDown")
    

            