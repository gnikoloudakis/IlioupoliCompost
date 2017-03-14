from models.models import Settings, Log, Errors
from Compost import app
import datetime
from flask_mongoengine import ValidationError
from flask import json


def addLog(message):
    success = False
    try:
        Log(timestamp=datetime.datetime.now(), action=message).save()
    except Exception as e:
        app.logger.error("error while inserting log action : " + str(e))
    else:
        success = True
    return success


def addError(message):
    success = False
    try:
        Errors(timestamp=datetime.datetime.now(), error=message).save()
    except Exception as e:
        app.logger.error("error while inserting error : " + str(e))
    else:
        success = True
    return success


def saveSettings(form):
    success = False
    try:
        Settings.objects.first().update(set__daily_soil_backward_time=form['sb_time'],
                                        set__daily_steering_time=form['time'],
                                        set__steering_duration=form['duration'],
                                        set__motor_F_duration=form['mf_time'],
                                        set__motor_B_duration=form['mb_time'],
                                        set__motor_R_duration=form['mr_time'],
                                        set__motor_L_duration=form['ml_time'],
                                        set__vent_duration=form['vent_time'],
                                        set__lowest_soil_humidity=form['lsht'],
                                        set__highest_soil_humidity=form['hsht'],
                                        set__highest_air_humidity_inside=form['hahit'],
                                        set__lowest_soil_temperature=form['lstt'],
                                        set__sleep_time_for_motors=form['sleep'])
    except Exception as e:
        addError("Cannot save settings ... :" + str(e))
    else:
        success = True
    return success


def getSettings():
    success = False
    a = []
    try:
        a = Settings.objects.first()
    except Exception as e:
        app.logger.error("Error while getting settings from database : " + str(e))
    else:
        success = True

    return success, a


def dropLog():
    success = False
    try:
        Log.drop_collection()
    except Exception as e:
        addError("could not drop Log collection" + str(e))
    else:
        success = True
    return success


def dropErrors():
    success = False
    try:
        Errors.drop_collection()
    except Exception as e:
        addError("could not drop Error collection" + str(e))
    else:
        success = True
    return success
