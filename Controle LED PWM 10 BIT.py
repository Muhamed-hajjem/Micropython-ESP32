from machine import Pin, PWM
from time import sleep


led = PWM(Pin(33))
led.freq(500)  

# Faire varier la luminosité
while True:
    for duty in range(0, 1024):  # Duty cycle de 0 à 1023
        led.duty(duty)
        sleep(0.01)
    for duty in range(1023, -1, -1):
        led.duty(duty)
        sleep(0.01)
