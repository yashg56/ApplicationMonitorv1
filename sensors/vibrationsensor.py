import RPi.GPIO as GPIO
import time
import smtplib
import sys

class State(object):
    def __init__(self, ON, OFF):
        self.ON = ON
        self.OFF = OFF
    
enum = State(1, 0)

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
callback_timestamp = time.time()
email_address = "noreplyappmonitornotifications@gmail.com"

def callback(channel):
    global callback_timestamp
    callback_timestamp = time.time()
    
"""def is_vibrating(channel):
    result = false
    
    if(GPIO.input(channel)):
       infinite_loop()
       result = true
       
    return result
"""
     
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, "corporatex")
    msg = "This is a test email!"
    server.sendmail(email_address, email_address, msg)
    server.quit()
    print("Sending mail...")
    time.sleep(20)

def infinite_loop():
    # infinite loop
    while True:                       #while is_vibrating:
        current_time = time.time()
        print(current_time)
        print(callback_timestamp)
        print("------------------------")

        if((current_time - callback_timestamp) > 10):
            send_mail()
            enum.OFF = 1
            
        if(enum.OFF == 1):
            sys.exit("Break: Sucessful Termination; Email Sent!")
            break
            

        
        time.sleep(1)
       
       
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change




