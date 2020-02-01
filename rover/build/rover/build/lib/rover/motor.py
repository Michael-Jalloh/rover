
class Motor(object):
    def __init__(self, name="motor"):
        self.name = name
        self.speed = 0
        self.direction = "f"
    
    def stop(self):
        self.direction = "s"
        self.speed =  0

    def forward(self):
        self.direction = "f"

    def backward(self):
        self.direction = "b"

    def shutdown(self):
        self.direction = "sh"

    def free_wheel(self):
        self.direction = "s"

    def set_speed(self, speed):
        self.speed = speed
    
    def get_data(self):
        return f"{self.speed}:{self.direction}"
    
