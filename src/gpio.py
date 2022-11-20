import RPi.GPIO as GPIO
import time

BURNER_PIN = 3 # connect relays to constant 5v pin 4
HEATER_PIN = 5 # connect relays to ground pin 6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BURNER_PIN, GPIO.OUT)
GPIO.setup(HEATER_PIN, GPIO.OUT)

def punch_relay():
    GPIO.output(BURNER_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BURNER_PIN, GPIO.LOW)

def heater_on():
    GPIO.output(HEATER_PIN, GPIO.HIGH)

def heater_off():
    GPIO.output(HEATER_PIN, GPIO.LOW)
