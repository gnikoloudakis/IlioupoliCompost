import serial

from Compost import app

ser = serial.Serial('/dev/ttyACM0', 9600)


# while 1:
#     ser.write('v\r\n'.encode())
#     time.sleep(1)
#     print(ser.readline())


def readVariables():
    # vars = ""
    try:
        ser.write('v\r\n'.encode())
    except Exception as e:
        app.logger.debug("error while reading variables :", e)
    else:
        vars = ser.readline()
        if vars.__len__() > 0:
            print(type(vars()))
            print(vars)
        else:
            print("poutsa pali")
