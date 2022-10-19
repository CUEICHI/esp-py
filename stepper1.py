#
#
# stepper  28BYJ-48

from machine import Pin
from time import sleep_ms,sleep

p1 = Pin(16,Pin.OUT)
p2 = Pin(17,Pin.OUT)
p3 = Pin(18,Pin.OUT)
p4 = Pin(19,Pin.OUT)

dly = 2

while True:
    
    p1.value(1)
    p2.value(1)
    p3.value(0)
    p4.value(0)
    sleep_ms(dly)

    p1.value(0)
    p2.value(1)
    p3.value(1)
    p4.value(0)
    sleep_ms(dly)

    p1.value(0)
    p2.value(0)
    p3.value(1)
    p4.value(1)
    sleep_ms(dly)

    p1.value(1)
    p2.value(0)
    p3.value(0)
    p4.value(1)
    sleep_ms(dly)


while True:
    
    p1.value(1)
    p2.value(0)
    p3.value(0)
    p4.value(0)
    sleep_ms(dly)

    p1.value(0)
    p2.value(1)
    p3.value(0)
    p4.value(0)
    sleep_ms(dly)

    p1.value(0)
    p2.value(0)
    p3.value(1)
    p4.value(0)
    sleep_ms(dly)

    p1.value(0)
    p2.value(0)
    p3.value(0)
    p4.value(1)
    sleep_ms(dly)

