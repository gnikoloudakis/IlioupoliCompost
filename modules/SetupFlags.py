import RPi.GPIO as gpio
import datetime
from ext import myFlags


def readFlags():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(6, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(13, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(19, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(26, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    Motor1 = gpio.input(5)
    Motor2 = gpio.input(6)
    Vent = gpio.input(13)
    Fan = gpio.input(19)
    Door = gpio.input(26)

    if Motor1:
        myFlags.Motor1 = True
    else:
        myFlags.Motor1 = False

    if Motor2:
        myFlags.Motor2 = True
    else:
        myFlags.Motor2 = False

    if Vent:
        myFlags.Vent = True
    else:
        myFlags.Vent = False

    if Fan:
        myFlags.Fan = True
    else:
        myFlags.Fan = False

    if Door:
        myFlags.Door = True
        from modules.MotorFunctions import StopMotors
        StopMotors()
    else:
        myFlags.Door = False
    gpio.cleanup()

    print ('Motor1: ' + str(Motor1) + ' Motor2: ' + str(Motor2) + ' Vent: ' + str(Vent) + ' Fan: ' + str(Fan) + ' Door: ' + str(Door) + ' time: ' + str(datetime.datetime.now()))
    # socketio.emit("flags", {'Motor1': Compost.Motor1, 'Motor2': Compost.Motor2, 'Vent': Compost.Vent, 'Fan': Compost.Fan, 'Door': Compost.Door})
    # gpio.add_event_detect(26, gpio.FALLING, callback=ff2, bouncetime=300)
    # return Motor1, Motor2, Vent, Fan, Door
