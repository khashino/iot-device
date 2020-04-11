#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import ConfigParser
import io

with open("/project/config.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

Buzzer = int(config.get('indicators', 'buzzer'))
led3 = int(config.get('indicators', 'led3'))
led1 = int(config.get('indicators', 'led1'))
led2 = int(config.get('indicators', 'led2'))

#####################BUZZER##################

def buzzersetup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(Buzzer, GPIO.OUT)


def buzzeron():
    GPIO.output(Buzzer, GPIO.HIGH)


def buzzeroff():
    GPIO.output(Buzzer, GPIO.LOW)


def beep(x):
    buzzersetup()
    buzzeron()
    time.sleep(x)
    buzzeroff()
    destroy()


#############LED###################



def ledsetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(led3, GPIO.OUT, initial=GPIO.LOW)


def ledon(led):
    GPIO.output(led, GPIO.HIGH)


def ledoff(led):
    GPIO.output(led, GPIO.LOW)


def blink(led, x):
    ledsetup()
    ledon(led)
    time.sleep(x)
    ledoff(led)
    destroy()

def blinkall(x):
    ledsetup()
    ledon(led1)
    ledon(led2)
    ledon(led3)
    time.sleep(x)
    ledoff(led1)
    ledoff(led2)
    ledoff(led3)
    destroy()

def destroy():

    # GPIO.output(BuzzerPin, GPIO.HIGH)

    GPIO.cleanup()  # Release resource
