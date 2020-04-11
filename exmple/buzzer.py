#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Buzzer = 40 

def setup(pin):
        global BuzzerPin
        BuzzerPin = pin
        GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
        GPIO.setup(BuzzerPin, GPIO.OUT)
        GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
        GPIO.output(BuzzerPin, GPIO.HIGH)

def off():
        GPIO.output(BuzzerPin, GPIO.LOW)

def beep(x):
        on()
        time.sleep(x)
        off()

def loop():
        while True:
                beep(0.03)
                time.sleep(1)
                beep(0.03)
                time.sleep(1)
                beep(0.03)
                time.sleep(1)
                beep(0.03)
                time.sleep(1)
                beep(0.03)
                time.sleep(1)
                beep(0.03)

                time.sleep(0.5)
                beep(0.03)
                time.sleep(0.5)
                beep(0.03)
                time.sleep(0.5)
                beep(0.03)
                time.sleep(0.5)
                beep(0.03)

                time.sleep(0.05)
                beep(0.03)
                time.sleep(0.05)
		beep(0.03)
		time.sleep(0.05)
                beep(0.03)
		time.sleep(0.05)
                beep(0.03)

		time.sleep(0.05)
                beep(2)



def destroy():
	GPIO.output(BuzzerPin, GPIO.HIGH)
	GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
	setup(Buzzer)
	try:
		loop()
	except KeyboardInterrupt: 
		destroy()