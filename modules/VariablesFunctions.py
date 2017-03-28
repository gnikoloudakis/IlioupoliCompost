import time

import serial

from Compost import app


def readVariables():
    ser = serial.Serial('/dev/ttyACM0',
                        baudrate=9600,
                        timeout=1
                        )
    ser.write('v\r\n'.encode())
    time.sleep(2)
    x = ser.readline()
    print x
    ser.close()
