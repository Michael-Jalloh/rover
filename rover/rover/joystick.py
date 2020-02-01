class JoyStick(object):
    def __init__(self, msg=None):
        self.cross = 0
        self.circle = 0
        self.triangle = 0
        self.square = 0
        self.share = 0
        self.options = 0
        self.dright = 0
        self.dleft = 0
        self.dup = 0
        self.ddown = 0
        self.lx = 0
        self.ly = 0
        self.l1 = 0
        self.l2 = 0
        self.l3 = 0
        self.rx = 0
        self.ry = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        if msg:
            self.update(msg)

    def update(self, msg):
        if(len(msg.buttons) < 1):
            return 
        self.cross = msg.buttons[0]
        self.circle = msg.buttons[1]
        self.triangle = msg.buttons[2]
        self.square = msg.buttons[3]
        self.share = msg.buttons[8]
        self.options = msg.buttons[9]
        

        self.dright = 1 if msg.axes[6] == -1 else 0
        self.dleft = 1 if msg.axes[6] == 1 else 0
        self.dup = 1 if msg.axes[7] == 1 else 0
        self.ddown = 1 if msg.axes[7] == -1 else 0
        self.lx = msg.axes[0]
        self.ly = msg.axes[1]
        self.l1 = msg.buttons[4]
        self.l2 = msg.axes[2]
        self.l3 = msg.buttons[11]
        self.rx = msg.axes[3]
        self.ry = msg.axes[4]
        self.r1 = msg.buttons[5]
        self.r2 = msg.axes[5]
        self.r3 = msg.buttons[12]


    def __repr__(self):
        return f"""\nUp: {self.dup} \nDown: {self.ddown} \nLeft: {self.dleft} \nRight: {self.dright} \nCross: {self.cross} \nCircle: {self.circle} \nTriangle: {self.triangle} \nSquare: {self.square}\nLx: {self.lx} \nLy: {self.ly} \nL1: {self.l1} \nL2: {self.l2} \nL3: {self.l3} \nRx: {self.rx} \nRy: {self.ry} \nR1: {self.r1} \nR2: {self.r2} \nR3: {self.r3} \nShare: {self.share} \nOptions: {self.options}"""