import RPi.GPIO as GPIO
import time
import smtplib
import sys
from state import State

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
callback_timestamp = time.time()
email_address = "noreplyappmonitornotifications@gmail.com"
current_state = State.INIT

def callback(channel):
    global callback_timestamp
    callback_timestamp = time.time()
    current_state = State.ACTIVE
     
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, "corporatex")
    msg = "This is a test email!"
    
    if(current_state == State.FINISHED):
        server.sendmail(email_address, email_address, msg)
        server.quit()
        print("Sending mail...")
        time.sleep(20)
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
while True:
    current_time = time.time()
    print(current_time)
    print(callback_timestamp)
    print("------------------------")

    if(current_state == State.FINISHED):
        if((current_time - callback_timestamp) > 10):
            current_state = State.FINISHED 
            send_mail()
            
            
    if(current_state == State.FINISHED):
        sys.exit("Break: Sucessful Termination; Email Sent!")
        break
            

        
    time.sleep(1)
       
       




