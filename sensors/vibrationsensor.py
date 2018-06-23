import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
    if GPIO.input(channel):
            print(GPIO.input(channel), end="")
    else:
            printf("To: ninadmore2@gmail.com\nFrom: RaspberryPi3\nSubject: Testing send mail from Raspberry\n\nThis is test. Best Regards!\n")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)
