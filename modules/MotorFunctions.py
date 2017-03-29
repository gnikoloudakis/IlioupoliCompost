import requests
import serial

import Compost
from Compost import app
from modules.DatabaseFunctions import addError, addLog
from modules.SetupFlags import readFlags


def Motor_1_Left():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Door:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/Motor_1_Left")
                ser.write('m1l\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while Motor_1_Left :", e)
                addError("Cannot start Motor 1 Left")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.error("Error while getting device (arduino) :", e)
            # addError("[Motor_1_Left] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Motor_1_Left] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Motor_1_Left] Door OPEN :")
        addError("[Motor_1_Left] Door OPEN")
    return success


def Motor_1_Right():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Door:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/Motor_1_Right")
                ser.write('m1r\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while Motor_1_Right :", e)
                addError("Cannot start Motor 1 Right")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.error("Error while getting device (arduino) :", e)
            # addError("[Motor_1_Right] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Motor_1_Right] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Motor_1_Right] Door OPEN :")
        addError("[Motor_1_Right] Door OPEN")
    return success


def Motor_2_Left():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Door:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/Motor_2_Left")
                ser.write('m2l\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while Motor_2_Left :", e)
                addError("Cannot start Motor 2 Left")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.error("Error while getting device (arduino) :", e)
            # addError("[Motor_2_Left] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Motor_2_Left] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Motor_2_Left] Door OPEN :")
        addError("[Motor_2_Left] Door OPEN")
    return success


def Motor_2_Right():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Door:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/Motor_2_Right")
                ser.write('m2r\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while Motor_2_Right :", e)
                addError("Cannot start Motor 2 Right")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.error("Error while getting device (arduino) :", e)
            # addError("[Motor_2_Right] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Motor_2_Right] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Motor_2_Right] Door OPEN :")
        addError("[Motor_2_Right] Door OPEN")
    return success


def Motor_1_Stop():
    success = False
    readFlags()  # diavazei ta flags
    try:
        # arduino = Devices.objects(name="arduino").first()
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        try:
            # requests.get("http://" + arduino.ip + ":8888/Motor_1_Stop")
            ser.write('m1stop\r\n'.encode())
        except requests.RequestException as e:
            app.logger.error("Error while Motor_1_Stop :", e)
            addError("Cannot stop Motor 1")
        else:
            success = True
            readFlags()  # diavazei ta flags
            ser.close()
    except Exception as e:
        # app.logger.error("Error while getting device (arduino) :", e)
        # addError("[Motor_1_Stop] Cannot find Arduino IP")
        app.logger.error("Error while setting up Serial :", e)
        addError("[Motor_1_Stop] Cannot setup Serial")
    return success


def Motor_2_Stop():
    success = False
    readFlags()  # diavazei ta flags
    try:
        # arduino = Devices.objects(name="arduino").first()
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        try:
            # requests.get("http://" + arduino.ip + ":8888/Motor_2_Stop")
            ser.write('m2stop\r\n'.encode())
        except requests.RequestException as e:
            app.logger.error("Error while Motor_2_Stop :", e)
            addError("Cannot stop Motor 2")
        else:
            success = True
            readFlags()  # diavazei ta flags
            ser.close()
    except Exception as e:
        # app.logger.error("Error while getting device (arduino) :", e)
        # addError("[Motor_2_Stop] Cannot find Arduino IP")
        app.logger.error("Error while setting up Serial :", e)
        addError("[Motor_2_Stop] Cannot setup Serial")
    return success


def StartFan():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Vent:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/StartFan")
                ser.write('startf\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while startFan() :", e)
                addError("Cannot start Fan")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.debug("Error while getting device (arduino) :", e)
            # addError("[StartFan] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Start Fan] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Start Fan] Vent ON :")
        addError("[Start Fan] Vent ON")
    return success


def StopFan():
    success = False
    readFlags()  # diavazei ta flags
    try:
        # arduino = Devices.objects(name="arduino").first()
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        try:
            # requests.get("http://" + arduino.ip + ":8888/StopFan")
            ser.write('stopf\r\n'.encode())
        except requests.RequestException as e:
            app.logger.error("Error while stopFan() :", e)
            addError("Cannot stop Fan")
        else:
            success = True
            readFlags()  # diavazei ta flags
            ser.close()
    except Exception as e:
        # app.logger.debug("Error while getting device (arduino) :", e)
        # addError("[StopFan] Cannot find Arduino IP")
        app.logger.error("Error while setting up Serial :", e)
        addError("[Stop Fan] Cannot setup Serial")
    return success


def StartVent():
    success = False
    readFlags()  # diavazei ta flags
    if not Compost.Fan:
        try:
            # arduino = Devices.objects(name="arduino").first()
            ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
            try:
                # requests.get("http://" + arduino.ip + ":8888/StartVent")
                ser.write('startv\r\n'.encode())
            except requests.RequestException as e:
                app.logger.error("Error while startVent() :", e)
                addError("Cannot start Vent")
            else:
                success = True
                readFlags()  # diavazei ta flags
                ser.close()
        except Exception as e:
            # app.logger.debug("Error while getting device (arduino) :", e)
            # addError("[StartVent] Cannot find Arduino IP")
            app.logger.error("Error while setting up Serial :", e)
            addError("[Start Vent] Cannot setup Serial")
        else:
            pass
    else:
        app.logger.error("[Start Vent] Fan ON :")
        addError("[Start Vent] Fan ON")
    return success


def StopVent():
    success = False
    readFlags()  # diavazei ta flags
    try:
        # arduino = Devices.objects(name="arduino").first()
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        try:
            # requests.get("http://" + arduino.ip + ":8888/StopVent")
            ser.write('stopv\r\n'.encode())
        except requests.RequestException as e:
            app.logger.error("Error while stopVent() :", e)
            addError("Cannot stop Vent")
        else:
            success = True
            readFlags()  # diavazei ta flags
            ser.close()
    except Exception as e:
        # app.logger.debug("Error while getting device (arduino) :", e)
        # addError("[StopVent] Cannot find Arduino IP")
        app.logger.error("Error while setting up Serial :", e)
        addError("[Stop Vent] Cannot setup Serial")
    return success


########################################################################################################

def StirForward():
    success = False
    if Motor_1_Left() and Motor_2_Right():
        app.logger.debug("Started stirring FORWARD")
        success = True
    else:
        app.logger.error("Could not Stir FORWARD")
        addError("[StirForward] Could NOT Stir FORWARD")
    return success


def StirBackward():
    success = False
    if Motor_1_Right() and Motor_2_Left():
        app.logger.debug("Started stirring BACKWARD")
        success = True
    else:
        app.logger.error("Could not Stir BACKWARD")
        addError("[StirBackward] Could NOT Stir BACKWARD")
    return success


def StirRight():
    success = False
    if Motor_1_Left() and Motor_2_Left():
        app.logger.debug("Started stirring RIGHT")
        success = True
    else:
        app.logger.error("Could not Stir RIGHT")
        addError("[StirRight] Could NOT Stir RIGHT")
    return success


def StirLeft():
    success = False
    if Motor_1_Right() and Motor_2_Right():
        app.logger.debug("Started stirring LEFT")
        success = True
    else:
        app.logger.error("Could not Stir LEFT")
        addError("[StirLeft] Could NOT Stir LEFT")
    return success


def StopMotors():
    success = False
    if Motor_1_Stop() and Motor_2_Stop():
        app.logger.debug("ALL motors STOPPED")
        addLog("[StopMotors] Motors STOPPED")
        success = True
    else:
        app.logger.error("Could NOT Stop motors")
        addError("[StopMotors] Could NOT Stop motors")
    return success

#############################################################################################
