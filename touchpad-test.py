from machine import TouchPad, Pin
from time import sleep_ms

t = TouchPad(Pin(12))
while True:
    print(t.read())
    sleep_ms(100)