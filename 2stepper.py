#stepper2

from machine import Pin
from time import sleep_ms,sleep

p1 = Pin(16,Pin.OUT)
p2 = Pin(17,Pin.OUT)
p3 = Pin(18,Pin.OUT)
p4 = Pin(19,Pin.OUT)

p5 = Pin(12,Pin.OUT)
p6 = Pin(13,Pin.OUT)
p7 = Pin(14,Pin.OUT)
p8 = Pin(15,Pin.OUT)

dly = 2

motor = [p1,p2,p3,p4]
motor2 = [p5,p6,p7,p8]
steps = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1]]

cnt=0
num = len(steps)

#while True:

for x in range(2048*2):
    for i,m in enumerate(motor):
        m.value(steps[cnt%num][3-i])
#        print(i,m,steps[cnt%num],steps[cnt%num][i])
    for i,m in enumerate(motor2):
        m.value(steps[cnt%num][3-i])
#        print(i,m,steps[cnt%num],steps[cnt%num][i])
    cnt+=1 
    print(cnt,steps[cnt%num])
    sleep_ms(dly)


for x in range(2048*2):
    for i,m in enumerate(motor):
        m.value(steps[cnt%num][i])
#        print(i,m,steps[cnt%num],steps[cnt%num][i])
    for i,m in enumerate(motor2):
        m.value(steps[cnt%num][i])
#        print(i,m,steps[cnt%num],steps[cnt%num][i])
    cnt+=1 
    sleep_ms(dly)



for m in motor:
    m.value(0)
for m in motor2:
    m.value(0)
    




