from machine import PWM,Pin
from time import sleep, sleep_ms

sw = Pin(22,Pin.IN,Pin.PULL_UP)

servo = PWM(Pin(15),freq=50) #50Hz 

i=20
while True:
    if sw.value() == 0:
        i =20 
        print(i)
    servo.duty(i)
    i+=1
    sleep(0.5)

 