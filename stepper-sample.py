from machine import Pin
from time import sleep_ms

dir = Pin(18,Pin.OUT)
step = Pin(16,Pin.OUT)


for i in range(100):
    dir.value(0)
    print(i)
    step.value(1)
    sleep_ms(20)
    step.value(0)
    sleep_ms(20)


for i in range(100):
    dir.value(1)
    print(i*-1)
    step.value(1)
    sleep_ms(20)
    step.value(0)
    sleep_ms(20)
