from flask import json
from ext import myFlags
from Compost import app
from models.models import Measurements


def add(jsondata):
    success = False
    a = json.loads(jsondata)
    try:
        Measurements(m_type=a['m_type'], m_value=a['m_value']).save()
    except Exception as e:
        app.logger.error("Error while inserting measurement  :", e)
    else:
        success = True
    return success

    # {"m_type":"type",
    #  "m_value":"value"}


def drop():
    success = False
    try:
        Measurements.drop_collection()
    except Exception as e:
        app.logger.error("Error while dropping measurements  :", e)
    else:
        success = True
    return success


def get(m_type):
    success = False
    m = []
    try:
        m = Measurements.objects(m_type=m_type).order_by("timestamp")
    except Exception as e:
        app.logger.error("error while getting measurements : ", e)
    else:
        success = True
    return success, json.dumps(m)


def getLast(m_type):
    success = False
    m = []
    # if m_type == 'outside_temp':
    #     print myFlags.air_temp_out
    #     m = {"m_type": m_type,
    #          "m_value": myFlags.air_temp_out}
    try:
        m = Measurements.objects(m_type=m_type).order_by("-timestamp").first()
    except Exception as e:
        app.logger.error("error while getting measurements : ", e)
    else:
        success = True
    return success, json.dumps(m)
