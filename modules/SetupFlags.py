import RPi.GPIO as gpio

from ext import myFlags


def readFlags():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(6, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(13, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(19, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    gpio.setup(26, gpio.IN)  # , pull_up_down=gpio.PUD_UP)
    if gpio.input(5):
        myFlags.Motor1 = True
    else:
        myFlags.Motor1 = False

    if gpio.input(6):
        myFlags.Motor2 = True
    else:
        myFlags.Motor2 = False

    if gpio.input(13):
        myFlags.Vent = True
    else:
        myFlags.Vent = False

    if gpio.input(19):
        myFlags.Fan = True
    else:
        myFlags.Fan = False

    if gpio.input(26):
        myFlags.Door = True
    else:
        myFlags.Door = False
    gpio.cleanup()
    # socketio.emit("flags", {'Motor1': Compost.Motor1, 'Motor2': Compost.Motor2, 'Vent': Compost.Vent, 'Fan': Compost.Fan, 'Door': Compost.Door})
    # gpio.add_event_detect(26, gpio.FALLING, callback=ff2, bouncetime=300)
    # return Motor1, Motor2, Vent, Fan, Door
