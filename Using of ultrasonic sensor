import RPi.GPIO as GPIO
import time.BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarning(False)
GPIO.setup(7,GPIO.OUT) #Trigger
GPIO.setup(11,GPIO.IN) #Echo
GPIO.output(7,False)
time.sleep(1)
GPIO.output(7,True)
time.sleep(0.001)
GPIO.output(7,False)
while GPIO input(11)==0:
          pulse_start=time.time()
while GPIO input(11)==1:
          pulse_stop=time.time()
pulse_duration = pulse_stop-pulse_start
distance=pulse_duration*17150
distance=round(distance,2)
print("Distance is:",distance,"cm")
GPIO.cleanup()
