import demjson
import serial


def readVariables():
    try:
        ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        x = ser.readline()
    except Exception as e:
        print ("exception while readVariables :", e)
    else:
        while x == "":
            ser.write('v\r\n'.encode())
            x = ser.readline()
        try:
            data = demjson.decode(x)
        except Exception as e:
            print ("read variables decode error: ", e)
        else:
            print (data['ato'])
            saveVariables(data)
        ser.close()


def saveVariables(data):
    pass
