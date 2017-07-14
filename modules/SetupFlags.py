import RPi.GPIO as gpio

from ext import myFlags

pin1 = 11
pin2 = 13
pin3 = 16
pin4 = 35
pin5 = 37
gpio.setmode(gpio.BOARD)
gpio.setup(pin1, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor1     pin11
gpio.setup(pin2, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor2     pin13
gpio.setup(pin3, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Vent       pin15
gpio.setup(pin4, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Fan        pin35
gpio.setup(pin5, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Door       pin37


def readFlags():
    # Motor1 = gpio.input(5)
    # Motor2 = gpio.input(6)
    # Vent = gpio.input(13)
    # Fan = gpio.input(19)
    # Door = gpio.input(26)

    if gpio.input(pin1):
        myFlags.Motor1 = True
        # print 'm1 HIGH'
    else:
        myFlags.Motor1 = False
        # print 'm1 LOW'

    if gpio.input(pin2):
        myFlags.Motor2 = True
        # print 'm2 HIGH'
    else:
        myFlags.Motor2 = False
        # print 'm2 LOW'

    if gpio.input(pin3):  #### HIGH for ON   LOW for OFF
        # print 'vent HIGH'
        myFlags.Vent = False
    else:
        myFlags.Vent = True  #### enw einai HIGH diavazei LOW??????s
        # print 'vent LOW'

    if gpio.input(pin4):
        myFlags.Fan = True
        # print 'fan HIGH'
    else:
        myFlags.Fan = False
        # print 'fan LOW'

    if gpio.input(pin5):
        myFlags.Door = True
        # print 'door HIGH'
    else:
        myFlags.Door = False
        # print 'door LOW'


        # print ('Motor1: ' + str(Motor1) + ' Motor2: ' + str(Motor2) + ' Vent: ' + str(not Vent) + ' Fan: ' + str(Fan) + ' Door: ' + str(Door) + ' time: ' + str(datetime.datetime.now()))
        # socketio.emit("flags", {'Motor1': Compost.Motor1, 'Motor2': Compost.Motor2, 'Vent': Compost.Vent, 'Fan': Compost.Fan, 'Door': Compost.Door})
        # gpio.add_event_detect(26, gpio.FALLING, callback=ff2, bouncetime=300)
        # return Motor1, Motor2, Vent, Fan, Door
