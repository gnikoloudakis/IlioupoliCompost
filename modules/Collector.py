import time

import serial


# from Compost import app


#
#
# def readVariables():
#     # vars = ""
#     try:
#         ser.write('v\r\n'.encode())
#     except Exception as e:
#         # app.logger.debug("error while reading variables :", e)
#         print "malakia paixtike!!"
#     else:
#         vars = ser.readline()
#         if vars.__len__() > 0:
#             print(type(vars()))
#             print(vars)
#         else:
#             print("poutsa pali")


def kolos():
    ser = serial.Serial('/dev/ttyACM0', 9600)

    ser.write('v\r\n'.encode())
    time.sleep(1)
    print ser.readline()
