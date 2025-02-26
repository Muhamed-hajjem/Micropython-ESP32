from machine import Pin as pin ,PWM
import time , utime 
trig = pin( 0 , pin.OUT , value = 0)
echo = pin( 1 , pin.IN)

v = 0.034
def ultrason():

    dis = em = rec = temps = 0 

    trig.on()
    utime.sleep_us(10)
    trig.off()

    while echo.value() == 0:
        em = utime.ticks_us()
    while echo.value() == 1 :
        rec = utime.ticks_us()
    

    temps = rec - em
    dis = int(v * temps /2 )
    return(dis)

while True : 
  distance = ultrason()
  print("Distance = ",distance)
  time.sleep(0.2)
  
  
