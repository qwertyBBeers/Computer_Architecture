import RPi.GPIO as GPIO
import time
button_1 = 27
led_1 = 26

dutytime = 0

GPIO.setup(button_1, GPIO.IN)

MOTER_A1_B=6
MOTER_A1_A=5
# MOTER_B1_B=21
# MOTER_B1_A=20

GPIO.setmode(GPIO.BCM)
p1 = GPIO.setup(MOTER_A1_B.GPIO.OUT)
p2 = GPIO.setup(MOTER_A1_A.GPIO.OUT)
# p3 = GPIO.setup(MOTER_B1_B.GPIO.OUT)
# p4 = GPIO.setup(MOTER_B1_A.GPIO.OUT)

p5 = GPIO.setup(led_1, GPIO.OUT)

p1.start(0)
p2.start(0)
# p3.start(0)
# p4.start(0)

p5.start(0)

try:
    while True:
        buttoninput = GPIO.input(button_1)
        if buttoninput == True:
            duty += 1
        else:
            duty -= 1
        
        if duty >99:
            duty = 100
        if duty <1:
            duty = 1
        p1.ChangeDutyCycle(duty)
        p2.ChangeDutyCycle(0)
        # p3.ChangeDutyCycle(duty)
        # p4.ChangeDutyCycle(0)
        
        p5.ChangeDutyCycle(duty)
except KeyboardInterrupt:

    pass

GPIO.cleanup()