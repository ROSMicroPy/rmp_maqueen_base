
import gc
import time
from machine import I2C, Pin

from ROSMicroPy import registerDataType, dumpDataType,registerEventSubscription,
from ROSMicroPy import run_ROS_Stack, init_ROS_Stack
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort

from rostype.Twist import Twist
from rostype.Attachment import Attachment

from mbits.lib.MaqueenDrive import MaqueenDrive

setNodeName("Turtle1")

i2c = I2C(1, scl=21, sda=22, freq=400000)
drive = MaqueenDrive(i2c)

def ros_event_callback(data):
    print(data)

    if (data["linear"]["x"] > 0):
        print("fwd")
        drive.forward(50)
    elif (data["linear"]["x"] < 0):
        print("Rev")
        drive.backward(50)
    elif (data["linear"]["x"] == 0):
        print("Stop")
        drive.stop()
        
    if (data["angular"]["y"] > 0):
        print("right")
        drive.turnRight(10, 0)
    elif (data["angular"]["y"] < 0):
        print("Rev")
        drive.turnLeft(10, 0)

        
def ros_attachment_callback(data):
    print(f"Attachment: [{data}]")
    print(data["attachment"])
    if (data["attachment"] == 1):
        drive.servoRun(0, 0)
    else:
        drive.servoRun(0, 105)
        

    
print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

print("Registgering Data Type\r\n")
typeTwist = registerDataType(Twist.dataMap)
dumpDataType(typeTwist)

typeAttach = registerDataType(Attachment.dataMap)
dumpDataType(typeAttach)

print("Registgering Event Subscription\r\n")
registerEventSubscription("/turtle1/cmd_vel", typeTwist, ros_event_callback)

print("Registgering Event Subscription\r\n")
registerEventSubscription("/turtle1/attachment", typeAttach, ros_attachment_callback)

print("Run ROS Stack\r\n")
run_ROS_Stack()  

#while True:
#    print("In Main Thread")
#    time.sleep(2)
    
    
    
    
    
    