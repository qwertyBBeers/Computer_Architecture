import RPi.GPIO as GPIO
import time
button_1 = 27
led_1 = 26
toggle = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(led_1, GPIO.OUT)

try:
    while True:
        buttoninput = GPIO.input(button_1)
        if buttoninput == 1 and toggle == 0:
            toggle = toggle + 1
            time.sleep(0.5)
        elif buttoninput == 1 and toggle == 1:
            toggle = 0
            time.sleep(0.5)

        if toggle == 1:
            GPIO.output(led_1, 1)
        elif toggle == 0:
            GPIO.output(led_1, 0)
except KeyboardInterrupt:

    pass

GPIO.cleanup()