#
# ADC 
#

from machine import Pin,ADC
from time import sleep_ms


sw = Pin(32,Pin.IN,Pin.PULL_UP) 
adc1 = ADC(Pin(34)) # 指定のピンについて ADC オブジェクトを作成
adc2 = ADC(Pin(35)) # 指定のピンについて ADC オブジェクトを作成
adc1.atten(ADC.ATTN_11DB)        
adc2.atten(ADC.ATTN_11DB)        



while True:
    val1 = adc1.read()
    val2 = adc2.read()
    i  = sw.value()
    print(val1/4,val2/4,i)
    sleep_ms(100)
