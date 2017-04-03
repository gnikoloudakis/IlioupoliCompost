import time

import RPi.GPIO as gpio


def testtt():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor1
    gpio.setup(6, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor2
    gpio.setup(13, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Vent
    gpio.setup(19, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Fan
    gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Door
    while 1:
        print ("Motor 1 : ", gpio.input(5))
        print ("Motor 2 : ", gpio.input(5))
        print ("Vent : ", gpio.input(5))
        print ("Fan : ", gpio.input(5))
        print ("Door : ", gpio.input(5))
        print ("\n####################################\n")

        time.sleep(.7)
        # gpio.cleanup()

testtt()
