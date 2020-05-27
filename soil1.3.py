import RPi.GPIO as GPIO
import time
import datetime
import signal
import sys


sensor_pin=17 
pump_pin=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin,GPIO.IN)
#GPIO.setup(pump_pin, GPIO.OUT,initial=1)
def kuiv_on():
    GPIO.setup(pump_pin, GPIO.OUT,initial=0)
    GPIO.output(pump_pin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(pump_pin, GPIO.LOW)  # Turn motor off
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor_pin,GPIO.IN)
    print("kastetud")
    f = open("päevik.txt", "a")
    f.write("Kastetud {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    f.close()

def m2rg_on():
    print("pole vaja kasta")
    f = open("päevik.txt", "a")
    f.write("pole vaja kasta {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    f.close()

while True:
    print("waiting for event")
    GPIO.wait_for_edge(sensor_pin, GPIO.BOTH, bouncetime=300)
    time.sleep(0.3)
    if GPIO.input(sensor_pin):
        kuiv_on()
    else:
        m2rg_on()
