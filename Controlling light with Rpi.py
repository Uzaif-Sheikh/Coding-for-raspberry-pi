import RPi.GPIO as GPIO
import time.BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarning(False)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
time.sleep(2)
GPIO.output()

#Second code:-

import RPi.GPIO as GPIO
import time.BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarning(False)
GPIO.setup(3,GPIO.out)
GPIO.setup(8,GPIO.out)
GPIO.setup(40,GPIO.out)
while True:
      GPIO.output(3,True)
      time.sleep(2)
      GPIO.output(3,false)
      time.sleep(2)

