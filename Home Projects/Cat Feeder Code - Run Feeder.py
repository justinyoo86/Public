import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def feeding_time():
	GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.output(3, GPIO.LOW)
	time.sleep(2)
	GPIO.output(3, GPIO.HIGH)

feeding_time()
print("Cats have been fed.")