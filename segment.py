import RPi.GPIO as GPIO
import time
delay = 0.09

x = 1
while x ==1:

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)


        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)


        GPIO.output(12, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(24, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(26, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(16, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(26, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(20, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)

        time.sleep(delay)

        GPIO.output(26, GPIO.HIGH)

        time.sleep(delay)

        GPIO.output(21, GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)

        time.sleep(delay)