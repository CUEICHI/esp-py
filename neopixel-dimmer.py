from machine import Pin
from time import sleep_ms
import neopixel
from random import randrange

NUM = 24
MAXCOL = 80
neopin = Pin(13,Pin.OUT)

neo = neopixel.NeoPixel(neopin,NUM)

while True:
    neo[0] = (randrange(MAXCOL),randrange(MAXCOL),randrange(MAXCOL))
    neo.write()
    sleep_ms(100)
    for i in range(1,NUM):
        #neo.fill((0,0,0))
        neo[i]=(int(neo[i-1][0]/1.2),int(neo[i-1][1]/1.2),int(neo[i-1][2]/1.2))
        neo[i-1]=(0,0,0)
        neo.write()
        print(i)
        sleep_ms(30)
