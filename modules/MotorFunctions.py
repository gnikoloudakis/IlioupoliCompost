import time

from Compost import app
from ext import myFlags
from modules.DatabaseFunctions import addError, addLog
from modules.SetupFlags import readFlags


def standardMotorFunction(serialcommand, func):
    x = ""
    success = True
    try:
        myFlags.ser.close()
        myFlags.ser.open()
    except Exception as e:
        app.logger.error("[" + func + "] Cannot Initialize Serial :", e)
        addError("[" + func + "] Cannot Initialize Serial")
    else:
        while x == "":
            x = myFlags.ser.readline()
            time.sleep(.5)
            myFlags.ser.write(serialcommand + '\r\n'.encode())
            print x
        addLog(func + "Started")
        success = True
        myFlags.ser.close()
    return success


def Motor_1_Left():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('12', 'Motor_1_Left')
    else:
        app.logger.error("[Motor_1_Left] Door OPEN :")
        addError("[Motor_1_Left] Door OPEN")
    return success


def Motor_1_Right():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('11', 'Motor_1_Right')
    else:
        app.logger.error("[Motor_1_Right] Door OPEN :")
        addError("[Motor_1_Right] Door OPEN")
    return success


def Motor_2_Left():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('22', 'Motor_2_Left')
    else:
        app.logger.error("[Motor_2_Left] Door OPEN :")
        addError("[Motor_2_Left] Door OPEN")
    return success


def Motor_2_Right():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('21', 'Motor_2_Right')
    else:
        app.logger.error("[Motor_2_Right] Door OPEN :")
        addError("[Motor_2_Right] Door OPEN")
    return success


def Motor_1_Stop():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('10', 'Motor_1_Stop')
    else:
        app.logger.error("[Motor_1_Stop] Door OPEN :")
        addError("[Motor_1_Stop] Door OPEN")
    return success


def Motor_2_Stop():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('20', 'Motor_2_Stop')
    else:
        app.logger.error("[Motor_2_Stop] Door OPEN :")
        addError("[Motor_2_Stop] Door OPEN")
    return success


def StartFan():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('31', 'StartFan')
    else:
        app.logger.error("[StartFan] Door OPEN :")
        addError("[StartFan] Door OPEN")
    return success


def StopFan():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('30', 'StopFan')
    else:
        app.logger.error("[StopFan] Door OPEN :")
        addError("[StopFan] Door OPEN")
    return success


def StartVent():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('41', 'StartVent')
    else:
        app.logger.error("[StartVent] Door OPEN :")
        addError("[StartVent] Door OPEN")
    return success


def StopVent():
    success = False
    readFlags()  # diavazei ta flags
    if not myFlags.Door:
        success = standardMotorFunction('40', 'StopVent')
    else:
        app.logger.error("[StopVent] Door OPEN :")
        addError("[StopVent] Door OPEN")
    return success


# ########################################################################################################

def StirForward():
    success = False
    if Motor_1_Left() and Motor_2_Right():
        app.logger.debug("Started stirring FORWARD")
        addLog("Started stirring FORWARD")
        success = True
    else:
        app.logger.error("Could not Stir FORWARD")
        addError("[StirForward] Could NOT Stir FORWARD")
    return success


def StirBackward():
    success = False
    if Motor_1_Right() and Motor_2_Left():
        app.logger.debug("Started stirring BACKWARD")
        addLog("Started stirring BACKWARD")
        success = True
    else:
        app.logger.error("Could not Stir BACKWARD")
        addError("[StirBackward] Could NOT Stir BACKWARD")
    return success


def StirRight():
    success = False
    if Motor_1_Left() and Motor_2_Left():
        app.logger.debug("Started stirring RIGHT")
        addLog("Started stirring RIGHT")
        success = True
    else:
        app.logger.error("Could not Stir RIGHT")
        addError("[StirRight] Could NOT Stir RIGHT")
    return success


def StirLeft():
    success = False
    if Motor_1_Right() and Motor_2_Right():
        app.logger.debug("Started stirring LEFT")
        addLog("Started stirring LEFT")
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

# #############################################################################################
