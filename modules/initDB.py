from models.models import Settings
from flask_mongoengine import ValidationError
from Compost import app


def initDb():
    success = False
    try:
        Settings(daily_soil_backward_time='06:00am',
                 daily_steering_time='14:00pm',
                 steering_duration='60',
                 motor_F_duration='60',
                 motor_B_duration='60',
                 motor_R_duration='60',
                 motor_L_duration='60',
                 vent_duration='300',
                 lowest_soil_humidity='55',
                 highest_soil_humidity='65',
                 highest_air_humidity_inside='85',
                 lowest_soil_temperature='50',
                 usb_port='/dev/cu.usbmodem1411',
                 sleep_time_for_motors='3').save()
        app.logger.debug("Initialized Settings")
    except Exception as e:
        app.logger.error("Failed to initialize settings :" + str(e))
    else:
        success = True
    return success
