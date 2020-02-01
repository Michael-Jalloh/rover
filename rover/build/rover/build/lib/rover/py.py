
import serial.tools.list_ports
from serial import Serial 
import sys
import atexit
import platform
from threading import Thread
from time import sleep


def findArduinoPort(verbose=False, show=False):
    if verbose:
        print("=== Auto scan for Arduino Uno connected port ===")
        print("")
        print(platform.system(), platform.release())
        print(platform.dist())
        print("Python version " + platform.python_version())
        print("")
    arduino_pids = ["VID:PID=1A86:7523", "VID:PID=2341:0043"]
    portList = list(serial.tools.list_ports.comports())
    arduinos = []
    for port in portList:
        if show:
            print("[*] {} ".format(port))
            print(port[0])
            print(port[1])
            print(port[2])
        print("=="*10)

        for pid in arduino_pids:
            
            if pid in port[0] \
                or pid in port[1]\
                or pid in port[2]:
                
                if verbose:
                    print("[*] {} ".format(port))
                    print(port[0])
                    print(port[1])
                    print(port[2])
                arduinos.append(port)

                #please note: it is not sure [0]
                #returned port[] is no particular order
                #so, may be [1], [2]
                return port[0]
            

class Py(object):
    def __init__(self, port, buadrate=9600):
        self.port = port
        self.buadrate = buadrate
        self.closed = True
        self.enableRead = True
        self.numChars = 32
        self.newData = False 
        self.receviedData = ""
        self.open()
       

    def start(self):
        self.enableRead = True
        Thread(target=self.read, args=()).start()

    def stop(self):
        self.enableRead = False

    def read(self):
        print("[*] INFO: Starting to read...")
        recvInProgress = False
        startMarker = b"<"
        endMarker = b">"
        ndr = 0
        while(self.enableRead):
            rc = self.serialPort.read()
            #print(rc)
            if (recvInProgress):
                if (rc != endMarker):
                    self.receviedData += rc
                else:
                    recvInProgress = False
                    self.newData = True
            elif(rc == startMarker):
                self.receviedData = b""
                recvInProgress = True

        print("[*] INFO: Stopping to read...")

    def write(self, data):
        self.serialPort.write(b"<")
        self.serialPort.write(str(data).encode())
        self.serialPort.write(b">")
    
    def get_data(self):
        if(self.newData):
            self.newData = False
            return self.receviedData
        return ""

    def close(self):
        try:
            self.stop()
            sleep(1)
            if(self.closed):
                self.closed = False
                self.serialPort.close()
                print("[*]INFO: port closed")
            else:
                print("[*]INFO: port already opened")
        except:
            pass
    
    def open(self):
        try:
            self.serialPort = Serial(self.port, self.buadrate, timeout=1)
            print("[*]INFO: Connection established...")
        except:
            pass