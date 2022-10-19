from machine import Pin
from time import sleep

sw1 = Pin(12,Pin.IN,Pin.PULL_UP)
sw2 = Pin(14,Pin.IN,Pin.PULL_UP)

while True:
    print(sw1.value(),sw2.value())
    sleep(0.1)

