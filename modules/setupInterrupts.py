import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)


def my_callback(channel):
    print ("Falling eventsds")


gpio.add_event_detect(17, gpio.FALLING, callback=my_callback, bouncetime=300)

