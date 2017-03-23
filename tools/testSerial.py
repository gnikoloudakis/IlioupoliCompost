import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

# while 1:
ser.write('v\r\n'.encode())
time.sleep(1)
print(ser.readline())
ser.close()

