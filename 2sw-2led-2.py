from machine import Pin
from time import sleep

led1 = Pin(22,Pin.OUT)
led2 = Pin(23,Pin.OUT)
sw1 = Pin(12,Pin.IN,Pin.PULL_UP)
sw2 = Pin(14,Pin.IN,Pin.PULL_UP)
ledState1 = 1
ledState2 = 1

while True:
    s = sw1.value()
    t = sw2.value()
#    print(s,t)

    if s==0:
        ledState1 = -1 * ledState1
        sleep(0.1)

    if t==0:
        ledState2 = -1 * ledState2
        sleep(0.1)
    print(ledState1,ledState2)

    if ledState2 == 1:
        led1.value(1)
    else:
        led1.value(0)

    if ledState1 == 1:
        led2.value(1)
    else:
        led2.value(0)
    sleep(0.1)
