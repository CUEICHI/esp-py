#

from machine import Pin
from time import sleep

led1 = Pin(22,Pin.OUT)
sw = Pin(12,Pin.IN,Pin.PULL_UP)

while True:
    s = sw.value()
    if s==0:
        led1.value(1)
    else:
        led1.value(0)
    sleep(0.1)