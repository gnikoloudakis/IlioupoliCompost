from models.models import Devices
from flask import json
from Compost import app
from flask_mongoengine import ValidationError


def add(jsondata):
    success = False
    a = json.loads(jsondata)
    try:
        Devices(name=a['name'], ip=a['ip']).save()
    except Exception as e:
        app.logger.error("Error while inserting device  :" + str(e))
    else:
        success = True
    return success

    # {"name":"name",
    #  "ip":"ip"}


def update(jsondata):
    success = False
    a = json.loads(jsondata)
    try:
        Devices.objects(name=a['name']).first().update(set__name=a['new_name'], set__ip=a['new_ip'])
    except Exception as e:
        app.logger.error("Error while updating device  :" + str(e))
    else:
        success = True
    return success

    # {"name": "name",
    #  "new_name": "new_name",
    #  "new_ip":"new_ip"}
