import demjson
from flask import json
import time
from string import rstrip
from ext import myFlags


def readVariables():
    x = ""
    # i = 0
    try:
        # ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        myFlags.ser.close()
        myFlags.ser.open()
    except Exception as e:
        print ("exception while readVariables :", e)
    else:
        while x == "":
            myFlags.ser.write('v\r\n'.encode())
            time.sleep(1)
            x = myFlags.ser.readlines()
            # print i
            print rstrip(x[0], '\n')
            # i += 1
        try:
            data = demjson.decode(rstrip(rstrip(x[0], '\n'), '\r'))
        except Exception as e:
            print ("read variables decode error: ", e)
        else:
            print (data)
            saveVariables(data)
            myFlags.ser.close()


def saveVariables(data):
    from modules.MeasurementsFunctions import add
    # myFlags.soil_temp = data['st']
    add(json.dumps({'m_type': 'soil_temp',
                    'm_value': data['st']}))
    # myFlags.soil_hum = data['sh']
    add(json.dumps({'m_type': 'soil_hum',
                    'm_value': data['sh']}))
    # myFlags.air_temp_in = data['ati']
    add(json.dumps({'m_type': 'air_temp',
                    'm_value': data['ati']}))
    # myFlags.air_hum_in = data['ahi']
    add(json.dumps({'m_type': 'air_hum',
                    'm_value': data['ahi']}))
    # myFlags.air_temp_out = data['ato']
    add(json.dumps({'m_type': 'outside_temp',
                    'm_value': data['ato']}))
    # myFlags.air_hum_out = data['aho']
    add(json.dumps({'m_type': 'outside_hum',
                    'm_value': data['aho']}))
    # myFlags.sunlight_out = data['slo']
    add(json.dumps({'m_type': 'outside_light',
                    'm_value': data['slo']}))
