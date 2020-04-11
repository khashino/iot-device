#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import hashlib
from datetime import datetime
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import indicators
import ConfigParser
import io
import sync
import ui
import threading

with open("/project/config.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

clockfile = config.get('other', 'clockfile')
sleeptimer = float(config.get('finger', 'sleeptimer'))
fingerwait = float(config.get('finger', 'fingerwait'))


usersfile = config.get('finger', 'usersfile')

def lines_that_start_with(string, fp):
    return [line for line in fp if line.startswith(string)]
## Search for a finger
##
#time.sleep(30)
## Tries to initialize the sensor
def fingerinit():
    while True:
        try:
            f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

            #print("pass")
            #print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
            return f
        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            pass
        #exit(1)


def fingerop(f):
    f.convertImage(0x01)

    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('No match found!')
        #indicators.blinkall(1)
        ui.alarm("Not Found",(255, 0, 0),(0, 255, 0))
        indicators.beep(1)
        #exit(0)
        return False
    else:
        print('Found template at position #' + str(positionNumber))
        print('The accuracy score is: ' + str(accuracyScore))
        indicators.beep(0.03)
        indicators.blinkall(0.1)
        ui.alarm("Success",(0, 255, 0),(255, 0, 0))
    ##  get user data   ##
        user = ""
        with open(usersfile, "r") as fp:
            for line in lines_that_start_with(str(positionNumber), fp):
                user = line.split(",")

        fname = user[1]
        lname = user[2]
        now = datetime.now()
        clocktime = now.strftime('%Y/%m/%d-%H:%M:%S')
        ## put data in file ##
        try:
            fl = open(clockfile, "a")
            clock_data = str(positionNumber) + "," + fname + "," + lname + "," + clocktime + ",0\n"
            print(clock_data)
            fl.write(clock_data)
            fl.close()
            indicators.beep(0.03)
        except Exception as e:
            raise

        print("sync")
        sync.resync()
        print("sync Done")
#    time.sleep(fingerwait)
        return True
