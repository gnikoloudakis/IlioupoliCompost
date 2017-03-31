import demjson
import serial
from flask import json
import time
from string import rstrip


def readVariables():
    x = ""
    i = 0
    try:
        ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        ser.flushInput()
        ser.flushOutput()
    except Exception as e:
        print ("exception while readVariables :", e)
    else:
        while x == "":
            ser.write('v\r\n'.encode())
            time.sleep(.5)
            x = ser.readlines()
            print i
            print rstrip(x[0], '\n')
            i += 1
        try:
            data = demjson.decode(rstrip(rstrip(x[0], '\n'), '\r'))
        except Exception as e:
            print ("read variables decode error: ", e)
        else:
            print (data)
        ser.close()


readVariables()
