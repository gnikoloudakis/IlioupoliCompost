import Exception as Exception
import requests

from Compost import app
from models.models import Devices
from modules.DatabaseFunctions import addError


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
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StirForward")
        except requests.RequestException as e:
            app.logger.error("Error while StirForward :", e)
            addError("Cannot start StirForward")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[StirForward] Cannot find Arduino IP")
    return success


def StirBackward():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StirBackward")
        except requests.RequestException as e:
            app.logger.error("Error while StirBackward :", e)
            addError("Cannot start StirBackward")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[StirBackward] Cannot find Arduino IP")
    return success


def StirRight():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StirRight")
        except requests.RequestException as e:
            app.logger.error("Error while StirRight :", e)
            addError("Cannot start StirRight")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[StirRight] Cannot find Arduino IP")
    return success


def StirLeft():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StirLeft")
        except requests.RequestException as e:
            app.logger.error("Error while StirLeft :", e)
            addError("Cannot start StirLeft")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[StirLeft] Cannot find Arduino IP")
    return success


def StopMotors():
    success = False
    try:
        arduino = Devices.objects(name="arduino").first()
        try:
            requests.get("http://" + arduino.ip + ":8888/StopMotors")
        except requests.RequestException as e:
            app.logger.error("Error while StopMotors :", e)
            addError("Cannot start StopMotors")
        else:
            success = True
    except Exception as e:
        app.logger.error("Error while getting device (arduino) :", e)
        addError("[StopMotors] Cannot find Arduino IP")
    return success
