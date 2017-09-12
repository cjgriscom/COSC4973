# Author: C. J. Griscom
# date: 5Sep2017
# class: Python/Pi
# purpose: To demonstrate GPIO functions
# input: - 
# output: - 
#
#===================================================================

# imports
import math # for PI, sines, cosines, etc
import sys # for a graceful exit
import os # to check if a datafile exists 
import time
import RPi.GPIO as GPIO # import GPIO

# define global constants and Booleans

LED_red = 17
LED_green = 27
LED_blue = 22


oldR = 0
oldG = 0
oldB = 0



# define functions 


def interpolate(ledR, ledG, ledB, R, G, B):
    global oldR
    global oldG
    global oldB
    for dc in range(0, 101, 1):
       ledR.ChangeDutyCycle(oldR*(100-dc)/100. + R*dc/100)
       ledG.ChangeDutyCycle(oldG*(100-dc)/100. + G*dc/100)
       ledB.ChangeDutyCycle(oldB*(100-dc)/100. + B*dc/100)
       time.sleep(0.08)
    oldR = R
    oldG = G
    oldB = B
   



# ===== Main Program =====



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Use RPI3 pinouts

GPIO.setup(LED_red  , GPIO.OUT) # Setup red pin as an output
GPIO.setup(LED_green, GPIO.OUT) # Setup green pin as an output
GPIO.setup(LED_blue , GPIO.OUT) # Setup blue pin as an output

ledR = GPIO.PWM(LED_red, 144)
ledR.start(0)
ledG = GPIO.PWM(LED_green, 144)
ledG.start(0)
ledB = GPIO.PWM(LED_blue, 144)
ledB.start(0)

try:
    while 1:
        interpolate(ledR, ledG, ledB, 100, 0, 0)
        interpolate(ledR, ledG, ledB, 100, 100, 0)
        interpolate(ledR, ledG, ledB, 0, 100, 0)
        interpolate(ledR, ledG, ledB, 0, 100, 100)
        interpolate(ledR, ledG, ledB, 0, 0, 100)
        interpolate(ledR, ledG, ledB, 100, 0, 100)

except KeyboardInterrupt:
    pass
ledR.stop()
ledG.stop()
ledB.stop()

GPIO.cleanup()

print('\n-- End of program --')



