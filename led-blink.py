import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

while True:
  GPIO.output(4,GPIO.HIGH)
  sleep(1)
  GPIO.output(4,GPIO.LOW)
  sleep(1)
