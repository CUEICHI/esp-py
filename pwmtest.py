#
#

from machine import Pin,PWM
from time import sleep_ms

pin = Pin(22)
led = PWM(pin)
led.duty(0)
def pwmtest():
    for i in range(50):
        print(i)
        led.duty(i*10)
        sleep_ms(50)

def pwmtest2():
    for i in range(50):
        print(i)
        led.duty(500-i*10)
        sleep_ms(50)

pwmtest()
sleep_ms(2000)

pwmtest2()
led.duty(0)
