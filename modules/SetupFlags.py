import RPi.GPIO as gpio

import Compost
from Compost import socketio


def readFlags():
    print "read flags"
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(6, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(13, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(19, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(26, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    if gpio.input(5):
        Compost.Motor1 = True
    else:
        Compost.Motor1 = False

    if gpio.input(6):
        Compost.Motor2 = True
    else:
        Compost.Motor2 = False

    if gpio.input(13):
        Compost.Vent = True
    else:
        Compost.Vent = False

    if gpio.input(19):
        Compost.Fan = True
    else:
        Compost.Fan = False

    if gpio.input(26):
        Compost.Door = True
    else:
        Compost.Door = False
    gpio.cleanup()
    # socketio.emit("flags", {'Motor1': Compost.Motor1, 'Motor2': Compost.Motor2, 'Vent': Compost.Vent, 'Fan': Compost.Fan, 'Door': Compost.Door})
    # gpio.add_event_detect(26, gpio.FALLING, callback=ff2, bouncetime=300)
    # return Motor1, Motor2, Vent, Fan, Door
