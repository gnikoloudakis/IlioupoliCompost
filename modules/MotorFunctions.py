from models.models import Devices
from modules.DatabaseFunctions import addError
from flask_mongoengine import ValidationError
from Compost import app
import requests


def Motor_1_Left():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_1_Left")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_1_Left :", e)
            addError("Cannot start Motor 1 Left")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_1_Left] Cannot find Arduino IP")
    return success


def Motor_1_Right():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_1_Right")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_1_Right :", e)
            addError("Cannot start Motor 1 Right")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_1_Right] Cannot find Arduino IP")
    return success


def Motor_2_Left():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_2_Left")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_2_Left :", e)
            addError("Cannot start Motor 2 Left")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_2_Left] Cannot find Arduino IP")
    return success


def Motor_2_Right():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_2_Right")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_2_Right :", e)
            addError("Cannot start Motor 2 Right")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_2_Right] Cannot find Arduino IP")
    return success


def Motor_1_Stop():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_1_Stop")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_1_Stop :", e)
            addError("Cannot stop Motor 1")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_1_Stop] Cannot find Arduino IP")
    return success


def Motor_2_Stop():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/Motor_2_Stop")
        except requests.RequestException as e:
            app.logger.error("Error while Motor_2_Stop :", e)
            addError("Cannot stop Motor 2")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[Motor_2_Stop] Cannot find Arduino IP")
    return success


def StartFan():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StartFan")
        except requests.RequestException as e:
            app.logger.error("Error while startFan() :", e)
            addError("Cannot start Fan")
        else:
            success = True
    except Exception as e:
        app.logger.debug("Error while getting device (arduino) :", e)
        addError("[StartFan] Cannot find Arduino IP")
    return success


def StopFan():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StopFan")
        except requests.RequestException as e:
            app.logger.error("Error while stopFan() :", e)
            addError("Cannot stop Fan")
        else:
            success = True
    except Exception as e:
        app.logger.debug("Error while getting device (arduino) :", e)
        addError("[StopFan] Cannot find Arduino IP")
    return success


def StartVent():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StartVent")
        except requests.RequestException as e:
            app.logger.error("Error while startVent() :", e)
            addError("Cannot start Vent")
        else:
            success = True
    except Exception as e:
        app.logger.debug("Error while getting device (arduino) :", e)
        addError("[StartVent] Cannot find Arduino IP")
    return success


def StopVent():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StopVent")
        except requests.RequestException as e:
            app.logger.error("Error while stopVent() :", e)
            addError("Cannot stop Vent")
        else:
            success = True
    except Exception as e:
        app.logger.debug("Error while getting device (arduino) :", e)
        addError("[StopVent] Cannot find Arduino IP")
    return success


def StirForward():
    app.logger.debug("Stir Forward")
    success1 = Motor_1_Left()
    if success1:
        app.logger.debug("Motor 1 Left started in Stir Forward")
    else:
        app.logger.error("Motor 1 Left failed to start  in Stir Forward")
    success2 = Motor_2_Right()
    if success2:
        app.logger.debug("Motor 2 Right started in Stir Forward")
    else:
        app.logger.error("Motor 2 Right Failed to start in Stir Forward")


def StirBackward():
    app.logger.debug("Stir Backward")
    success1 = Motor_1_Right()
    if success1:
        app.logger.debug("Motor 1 Right started in Stir Backward")
    else:
        app.logger.error("Motor 1 Right failed to start  in Stir Backward")
    success2 = Motor_2_Left()
    if success2:
        app.logger.debug("Motor 2 Left started in Stir Backward")
    else:
        app.logger.error("Motor 2 Left Failed to start in Stir Backward")


def StirRight():
    app.logger.debug("Stir Right")
    success1 = Motor_1_Left()
    if success1:
        app.logger.debug("Motor 1 Left started in Stir Right")
    else:
        app.logger.error("Motor 1 Left failed to start  in Stir Right")
    success2 = Motor_2_Left()
    if success2:
        app.logger.debug("Motor 2 Left started in Stir Right")
    else:
        app.logger.error("Motor 2 Left Failed to start in Stir Right")


def StirLeft():
    app.logger.debug("Stir Left")
    success1 = Motor_1_Right()
    if success1:
        app.logger.debug("Motor 1 Right started in Stir Stir Left")
    else:
        app.logger.error("Motor 1 Right failed to start  in Stir Left")
    success2 = Motor_2_Right()
    if success2:
        app.logger.debug("Motor 2 Right started in Stir Left")
    else:
        app.logger.error("Motor 2 Right Failed to start in Stir Left")


def StopMotors():
    app.logger.debug("Stop All motors")
    success1 = Motor_1_Stop()
    if success1:
        app.logger.debug("Motor 1 stopped in StopAll")
    else:
        app.logger.error("Motor 1 failed to Stop  in StopAll")
    success2 = Motor_2_Stop()
    if success2:
        app.logger.debug("Motor 2 stopped in StopAll")
    else:
        app.logger.error("Motor 2 failed to Stop  in StopAll")
