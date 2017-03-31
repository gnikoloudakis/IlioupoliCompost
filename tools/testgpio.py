import time
import serial
from string import rstrip
import demjson

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)


def testtt():
    x = ""
    i = 0
    try:
        ser.close()
        ser.open()
    except Exception as e:
        print ("exception while testgpio :", e)
    else:
        while x is not 'Motor_1_Stop\r\n':
            ser.write('10\r\n'.encode())
            time.sleep(2)
            x = str(ser.readlines())
            print i
            print x
            i += 1
        ser.close()


testtt()
