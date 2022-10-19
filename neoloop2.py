from machine import Pin
from time import sleep_ms
import neopixel
from random import randrange

NUM = 24
MAXCOL = 20
neopin = Pin(13,Pin.OUT)

neo = neopixel.NeoPixel(neopin,NUM)

for i in range(NUM):
    neo[i] = (randrange(MAXCOL),randrange(MAXCOL),randrange(MAXCOL))
neo.write()


while True:
    for i in range(NUM-2,-1,-1):
        neo[i+1] = neo[i]
        print(i)
#        sleep_ms(100)
    neo[0] =  (randrange(MAXCOL),randrange(MAXCOL),randrange(MAXCOL))
    neo.write()
    sleep_ms(100)


while True:
    for i in range(NUM-1):
        neo[i] = neo[i+1]
    neo[NUM-1] =  (randrange(MAXCOL),randrange(MAXCOL),randrange(MAXCOL))
    neo.write()
    sleep_ms(50)