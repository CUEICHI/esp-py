#
#

from machine import Pin,PWM
from time import sleep_ms

pin1 = Pin(15)
pin2 = Pin(23)
led1 = PWM(pin1)
led2 = PWM(pin2)
led1.duty(0)
led2.duty(0)

def pwmtest():
    for i in range(50):
        print(i)
        led1.duty(i*10)
        led2.duty(500-i*10)
        sleep_ms(50)

def pwmtest2():
    for i in range(50):
        print(i)
        led1.duty(500-i*10)
        led2.duty(i*10)
        sleep_ms(50)

while True:
    pwmtest()
    sleep_ms(100)
    pwmtest2()

led1.duty(0)
led2.duty(0)

