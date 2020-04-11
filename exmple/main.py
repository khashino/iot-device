#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import os
from datetime import datetime
import math
import multiprocessing
from multiprocessing import Pool, TimeoutError
import hashlib

# from threading import Thread

import thread
import time
from pyfingerprint.pyfingerprint import PyFingerprint

#####################BUZZER##################
Buzzer = 40


def buzzersetup(pin):
    global BuzzerPin
    BuzzerPin = pin
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)
    #GPIO.output(BuzzerPin, GPIO.HIGH)


def buzzeron():
    GPIO.output(BuzzerPin, GPIO.HIGH)


def buzzeroff():
    GPIO.output(BuzzerPin, GPIO.LOW)


def beep(x):
    buzzeron()
    time.sleep(x)
    buzzeroff()


def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()  # Release resource


#############LED###################

led1 = 36
led2 = 32
led3 = 38


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
    ledon(led)
    time.sleep(x)
    ledoff(led)


def destroy():

    # GPIO.output(BuzzerPin, GPIO.HIGH)

    GPIO.cleanup()  # Release resource


#############finger###################

try:
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword() == False:
        raise ValueError('The given fingerprint sensor password is wrong!'
                         )
except Exception, e:

    print 'The fingerprint sensor could not be initialized!'
    print 'Exception message: ' + str(e)
    exit(0x01)


def enrollfinger():
    try:
        print 'Waiting for finger...'
        while f.readImage() == False:

            # pass

            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0x00000000]
        accuracyScore = result[0x01]
        if positionNumber == -0x01:
            print 'No match found!'
            time.sleep(2)
            return
        else:
            print 'Found template at position #' + str(positionNumber)
    except Exception, e:

        print 'Operation failed!'
        print 'Exception message: ' + str(e)
        exit(0x01)



def searchfinger():
	#print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

	## Tries to search the finger and calculate hash
	try:
	    print('Waiting for finger...')

	    ## Wait that finger is read
	    while ( f.readImage() == False ):
	        pass

	    ## Converts read image to characteristics and stores it in charbuffer 1
	    f.convertImage(0x01)

	    ## Searchs template
	    result = f.searchTemplate()

	    positionNumber = result[0]
	    accuracyScore = result[1]
	
	    if ( positionNumber == -1 ):
	        print('No match found!')
	        exit(0)
	    else:
	        print('Found template at position #' + str(positionNumber))
	        print('The accuracy score is: ' + str(accuracyScore))
	
	    ## OPTIONAL stuff
	    ##

	    ## Loads the found template to charbuffer 1
	    #f.loadTemplate(positionNumber, 0x01)
	
	    ## Downloads the characteristics of template loaded in charbuffer 1
	    #characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
	
	    ## Hashes characteristics of template
	    #print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
	
	except Exception as e:
	    print('Operation failed!')
	    print('Exception message: ' + str(e))
	    exit(1)
	

#############main#####################

if __name__ == '__main__':  # Program start from here
    buzzersetup(Buzzer)
    ledsetup()
    for x in range(1, 2):
	    blink(led2, 1)
	    blink(led3, 1)
	    blink(led1, 1)
    #time.sleep(0x01)
    beep(0.03)

    #while True:
    #    print 'loop'
    searchfinger()
    beep(0.03)
    destroy()

