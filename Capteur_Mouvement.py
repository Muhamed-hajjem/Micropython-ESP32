from machine import Pin as pin , PWM
from time import sleep
Mov = pin(0 , pin.IN )

while True :
  if Mov.value() == 0 :
    print("il y a du Mouvement")
  else :
    print("pas de mouvement ")
