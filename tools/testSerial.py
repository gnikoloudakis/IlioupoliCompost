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
        ser.close()
        ser.open()
    except Exception as e:
        print ("exception while readVariables :", e)
    else:
        while x == "":
            ser.write('v\r\n'.encode())
            time.sleep(.5)
            x = ser.readline()
            print i
            print (x)
            i += 1
        ser.close()
        try:
            data = json.loads(x)
        except Exception as e:
            print ("read variables decode error: ", e)
        else:

            print ('variables ok')
            print (data['slo'])


readVariables()
