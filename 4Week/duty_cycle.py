import RPi.GPIO as GPIO
import time
MotorB_APWM = 5
MotorB_B = 6

GPIO.setmede(GPIO.BCM)
GPIO.setup(MotorB_APWM, GPIO.OUT)
GPIO.setup(MotorB_B,GPIO.OUT)

p = GPIO.PWM(MotorB_APWM,20)
p.start(0)

duty=0
try:
    while True:
        for duty in range(0,101,20):
            p.ChangeDutyCycle(duty)
            time.sleep(0.1)
        for duty in range(100,-1,-20):
            p.ChangeDutyCycle(duty)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.Cleanup()