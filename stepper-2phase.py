#stepper2

from machine import Pin
from time import sleep_ms,sleep

p1 = Pin(16,Pin.OUT)
p2 = Pin(17,Pin.OUT)
p3 = Pin(18,Pin.OUT)
p4 = Pin(19,Pin.OUT)

dly = 1

motor = [p1,p2,p3,p4]

steps = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]]

cnt=0
num = len(steps)

while True:
    for i,m in enumerate(motor):
        m.value(steps[cnt%num][i])
        print(i,m,steps[cnt%num],steps[cnt%num][i])
    cnt+=1 
    sleep_ms(dly)





