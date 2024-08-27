from mbits.lib.MaqueenDrive import MaqueenDrive
from machine import I2C, Pin
import time
#i2c = I2C(0, scl=Pin(19), sda=Pin(20), freq=400000)
i2c = I2C(1, scl=21, sda=22, freq=400000)
#i2c = I2C(1, scl=Pin(21), sda=Pin(22), freq=400000)

#i2c = I2C(1, scl=19, sda=20, freq=100000, timeout=50000)   

drive = MaqueenDrive(i2c)
#drive.forward(50)
drive.servoRun(0, 105)
time.sleep(1)
drive.servoRun(0, 0)
time.sleep(1)
drive.servoRun(0, 105)
