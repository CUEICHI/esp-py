#
#
# 2led-b.py
#

from machine import Pin
from time import sleep

led1 = Pin(22,Pin.OUT)
led2 = Pin(23,Pin.OUT)

while True:
    led1.value(1)
    led2.value(0)
    sleep(0.5)
    led1.value(0)
    led2.value(1)
    sleep(0.5)




