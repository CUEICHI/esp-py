from machine import Pin,ADC
from time import sleep_ms

vol = ADC(Pin(32),atten=ADC.ATTN_11DB)

while True:
    print(vol.read_u16()/64)
    sleep_ms(100)
    