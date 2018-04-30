import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print "Movement Detected!"
        else:
                print "Movement Detected!"
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)import RPi.GPIO as GPIO
import time
import math as m 

class Sw40(object):
    """docstring for Senal"""
    def __init__(self, pin , led):
        self.led = led
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led,GPIO.OUT)
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=1)
        self.count = 0 

    def callback(self , pin):
        self.count += 1

    def LedOn(self):
        GPIO.output(self.led , 1)

    def LedOff(self):
        GPIO.output(self.led , 0)








def main():
    sensor = Sw40(21,20) 
    try:
        while True:

            time.sleep(1)
            if sensor.count >=1000:
                sensor.LedOn()
            else:
                sensor.LedOff()
            sensor.count = 0        



    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()