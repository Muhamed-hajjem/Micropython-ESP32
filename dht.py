from machine import Pin as pin ,ADC
import dht
from time import sleep

sensor = dht.DHT22(pin(4)) 
ledr = pin(14 , pin.OUT)
ledv = pin(12 , pin.OUT)
ledj = pin(33 ,pin.OUT)

while True :
    sensor.measure()

    temp = sensor.temperature()
    humidity = sensor.humidity()

    if ( 0 <= humidity<33):
        ledr.on()
    if (33<= humidity <70):
        ledj.on()
    if (70<= humidity <= 99):
        ledv.on()

  

   
