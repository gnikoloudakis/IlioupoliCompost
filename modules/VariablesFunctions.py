# import time
import serial
import demjson
from Compost import socketio


def readVariables():
    ser = serial.Serial('/dev/ttyACM0',
                        baudrate=9600,
                        timeout=1
                        )
    ser.write('v\r\n'.encode())
    # time.sleep(2)
    x = ser.readline()
    while x == "":
        ser.write('v\r\n'.encode())
        # time.sleep(2)
        x = ser.readline()
    try:
        data = demjson.decode(x)
    except Exception as e:
        print ("read variables decode error: ", e)
    else:
        print (data)
        socketio.emit("measurements", data)
    ser.close()
