import RPi.GPIO as GPIO
import time
button_1 = 27
led_1 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(led_1, GPIO.OUT)

try:
    while True:
        buttoninput = GPIO.input(button_1)
        GPIO.output(led_1,buttoninput)

except KeyboardInterrupt:

    pass

GPIO.cleanup()