import RPi.GPIO as GPIO
import time
button_1 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_1, GPIO.IN)

try:
    while True:
        buttoninput = GPIO.input(button_1)
        print(buttoninput)
        time.sleep(0.5)

except KeyboardInterrupt:

    pass

GPIO.cleanup()