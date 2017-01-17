# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led1 = 6  # GPIO number where the led is connected
led2 = 13
led3 = 26
source = 19
# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)


# Set GPIO no 10 to output mode
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(source, GPIO.OUT)

GPIO.output(led1, True)
GPIO.output(led2, True)
GPIO.output(led3, True)
GPIO.output(source, True)



# Blink some leds
try:
    while True:
        GPIO.output(led1, False)
        sleep(1)  # Sleep for 1 second
        GPIO.output(led1, True)
        GPIO.output(led2, False)
        sleep(1)
        GPIO.output(led2, True)
        GPIO.output(led3, False)
        sleep(1)
        GPIO.output(led3, True)
except:
    GPIO.cleanup()
