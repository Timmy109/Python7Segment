import RPi.GPIO as GPIO
import time
        
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