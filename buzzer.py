from machine import Pin as pin ,PWM
import time , utime 
bips = PWM(pin(15))
bips.freq(6000)
def bip ():
    bips.duty_u16(65533)
    time.sleep(0.5)
    bips.duty_u16(0)

while True :
    bip()
