from machine import Pin as pin ,PWM
import utime , time 

servo = PWM(pin(2))
servo.freq(50)

def angle (d,f):
    
    d1 = ((d * 65)/1.8) + 1500
    f1 = ((f * 65)/1.8) + 1500
    servo.duty_u16(int(d1))
    utime.sleep(1)
    servo.duty_u16(int(f1))
    utime.sleep(1)

while True :
  angle(0,90)
  time.sleep(2)
  angle(0,0)
  time.sleep(0.5)
