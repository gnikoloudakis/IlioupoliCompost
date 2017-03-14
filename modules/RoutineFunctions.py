from datetime import time
from models.models import Settings
from Compost import app


def pushSoilBack():
    from modules.MotorFunctions import StirBackward, StopMotors
    StirBackward()
    app.logger.debug("Started Motor Backward")
    time.sleep(int(Settings.objects.first().motor_B_duration))
    StopMotors()
    app.logger.debug("Started Motor Backward")


def pushSpoilForward():
    from modules.MotorFunctions import StirForward, StopMotors
    StirForward()
    app.logger.debug("Started Motor Forward")
    time.sleep(int(Settings.objects.first().motor_F_duration))
    StopMotors()
    app.logger.debug("Started Motor Forward")


def hourlyVentilation():
    from modules.MotorFunctions import StartVent, StopVent
    StartVent()
    app.logger.debug("Started hourly Ventilation")
    time.sleep(int(Settings.objects.first().vent_duration))
    StopVent()
    app.logger.debug("Stopped hourly Ventilation")


def soilHomogenization():
    from modules.MotorFunctions import StirRight, StirLeft, StopMotors, StartFan, StopFan
    StirRight()
    StartFan()
    app.logger.debug("Started soil Homogenization")
    time.sleep(int(Settings.objects.first().motor_R_duration))
    StopMotors()
    StirLeft()
    time.sleep(int(Settings.objects.first().motor_L_duration))
    StopMotors()
    StopFan()
    app.logger.debug("Stopped soil Homogenization")
