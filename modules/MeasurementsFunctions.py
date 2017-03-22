from flask import json

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


def get(jsondata):
    success = False
    m = []
    try:
        m = Measurements.objects(m_type=jsondata).order_by("timestamp")
    except Exception as e:
        app.logger.error("error while getting measurements : ", e)
    else:
        success = True
    return success, json.dumps(m)
