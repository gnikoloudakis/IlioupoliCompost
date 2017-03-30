import demjson
import serial
from flask import json


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
            print (data)
            saveVariables(data)
        ser.close()


def saveVariables(data):
    from modules.MeasurementsFunctions import add
    add(json.dumps({'m_type': 'soil_temp',
                    'm_value': data['st']}))
    add(json.dumps({'m_type': 'soil_hum',
                    'm_value': data['sh']}))
    add(json.dumps({'m_type': 'air_temp',
                    'm_value': data['ati']}))
    add(json.dumps({'m_type': 'air_hum',
                    'm_value': data['ahi']}))
    add(json.dumps({'m_type': 'outside_temp',
                    'm_value': data['ato']}))
    add(json.dumps({'m_type': 'outside_hum',
                    'm_value': data['aho']}))
    add(json.dumps({'m_type': 'outside_light',
                    'm_value': data['slo']}))
