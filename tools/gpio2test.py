# #!/usr/bin/env python
#
# from time import sleep  # Allows us to call the sleep function to slow down our loop
# import RPi.GPIO as GPIO  # Allows us to call our GPIO pins and names it just GPIO
#
# GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
# INPUT_PIN = 26  # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
# GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set our input pin to be an input
#
# # Start a loop that never ends
# while True:
#     if (GPIO.input(INPUT_PIN) == True):  # Physically read the pin now
#         print('HIGH')
#     else:
#         print('LOW')
#     sleep(1);  # Sleep for a full second before restarting our loop

import time

import RPi.GPIO as gpio

from ext import myFlags

# from modules.MotorFunctions import StopMotors
pin1 = 11
pin2 = 13
pin3 = 33#oiooioioi
pin4 = 35
pin5 = 37
gpio.setmode(gpio.BOARD)
gpio.setup(pin1, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor1
gpio.setup(pin2, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Motor2
gpio.setup(pin3, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Vent
gpio.setup(pin4, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Fan
gpio.setup(pin5, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Door


def readFlags():
    # Motor1 = gpio.input(5)
    # Motor2 = gpio.input(6)
    # Vent = gpio.input(13)
    # Fan = gpio.input(19)
    # Door = gpio.input(26)

    if gpio.input(pin1):
        myFlags.Motor1 = True
        print 'm1 HIGH'
    else:
        myFlags.Motor1 = False
        print 'm1 LOW'

    if gpio.input(pin2):
        myFlags.Motor2 = True
        print 'm2 HIGH'
    else:
        myFlags.Motor2 = False
        print 'm2 LOW'

    if gpio.input(pin3):  #### HIGH for ON   LOW for OFF
        print 'vent HIGH'
        myFlags.Vent = False
    else:
        myFlags.Vent = True  #### enw einai HIGH diavazei LOW??????s
        print 'vent LOW'

    if gpio.input(pin4):
        myFlags.Fan = True
        print 'fan HIGH'
    else:
        myFlags.Fan = False
        print 'fan LOW'

    if gpio.input(pin5):
        myFlags.Door = True
        print 'door HIGH'
    else:
        myFlags.Door = False
        print 'door LOW'


while 1:
    print "\n#############################################\n"
    readFlags()
    time.sleep(2)
    print "\n#############################################\n"
