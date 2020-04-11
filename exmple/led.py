#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)


GPIO.output(36, GPIO.HIGH)
time.sleep(1)
GPIO.output(36, GPIO.LOW)

GPIO.output(32, GPIO.HIGH)
time.sleep(1)
GPIO.output(32, GPIO.LOW)

GPIO.output(38, GPIO.HIGH)
time.sleep(1)
GPIO.output(38, GPIO.LOW)
