import serial


# from modules.DatabaseFunctions import addError

class myFlags(object):
    # Globals
    Motor1 = False
    Motor2 = False
    Fan = False
    Vent = False
    Door = False

    soil_temp = 0.0
    soil_hum = 0.0
    air_temp_in = 0.0
    air_hum_in = 0.0
    air_temp_out = 0.0
    air_hum_out = 0.0
    sunlight_out = 0.0

    try:
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    except Exception as e:
        print("could NOt setup SERIAL port")
    else:
        print("[ext.py] Initialized SERIAL port")
