import RPi.GPIO as gpio
import datetime
from ext import myFlags

# from modules.MotorFunctions import StopMotors

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor1
gpio.setup(6, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor2
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Vent
gpio.setup(19, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Fan
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Door


def readFlags():
    # Motor1 = gpio.input(5)
    # Motor2 = gpio.input(6)
    # Vent = gpio.input(13)
    # Fan = gpio.input(19)
    # Door = gpio.input(26)

    if gpio.input(5):
        myFlags.Motor1 = True
        # print 'm1 HIGH'
    else:
        myFlags.Motor1 = False
        # print 'm1 LOW'

    if gpio.input(6):
        myFlags.Motor2 = True
        # print 'm2 HIGH'
    else:
        myFlags.Motor2 = False
        # print 'm2 LOW'

    if gpio.input(21):  #### HIGH for ON   LOW for OFF
        # print 'vent HIGH'
        myFlags.Vent = False
    else:
        myFlags.Vent = True        #### enw einai HIGH diavazei LOW??????s
        # print 'vent LOW'

    if gpio.input(19):
        myFlags.Fan = True
        # print 'fan HIGH'
    else:
        myFlags.Fan = False
        # print 'fan LOW'

    if gpio.input(26):
        myFlags.Door = True
        # print 'door HIGH'
    else:
        myFlags.Door = False
        # print 'door LOW'
    # gpio.cleanup()

    # print ('Motor1: ' + str(Motor1) + ' Motor2: ' + str(Motor2) + ' Vent: ' + str(not Vent) + ' Fan: ' + str(Fan) + ' Door: ' + str(Door) + ' time: ' + str(datetime.datetime.now()))
    # socketio.emit("flags", {'Motor1': Compost.Motor1, 'Motor2': Compost.Motor2, 'Vent': Compost.Vent, 'Fan': Compost.Fan, 'Door': Compost.Door})
    # gpio.add_event_detect(26, gpio.FALLING, callback=ff2, bouncetime=300)
    # return Motor1, Motor2, Vent, Fan, Door
