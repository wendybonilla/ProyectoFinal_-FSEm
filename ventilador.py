#Proyecto Final Invernadero
# author: Casasola Hernandez Paulina
#         Barrera Rangel Guillermo
#         Bonilla Martinez Guadalupe Wendy
#
# ventilador.py
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from random import randint

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up pin no. 32 as output and default it to low
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)# ok
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)# riego
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #ventilador
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #foco
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) #Sensor de Temperatura
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) #sensor de humedad

def estable(tem,hum):
    print('Condiciones estables\n')
    
def HumBajo(tem,hum):
    print('Enceder riego\n')
    sleep(1)                
    GPIO.output(16, GPIO.HIGH) 
    sleep(5)                 
    GPIO.output(16, GPIO.LOW)  

def HumAlto(tem,hum):
    print('Enceder foco y ventilador\n')
    sleep(1)                 
    GPIO.output(22, GPIO.HIGH) 
    GPIO.output(18, GPIO.HIGH)
    sleep(5)                 
    GPIO.output(22, GPIO.LOW)  
    GPIO.output(18, GPIO.LOW)
    
def TemBajo(tem,hum):
    print('Enceder foco\n')
    sleep(1)                
    GPIO.output(22, GPIO.HIGH) 
    sleep(5)                 
    GPIO.output(22, GPIO.LOW) 
    
def TemAlta(tem,hum):
    print('\n Enceder ventilador\n')
    sleep(1)                
    GPIO.output(18, GPIO.HIGH) 
    sleep(5)                 
    GPIO.output(18, GPIO.LOW) 
    

# Blink the led
while True: # Forever
    tem = randint(10,30)
    hum = randint(45,100)
    if (tem>=10)and(tem<=25):
       if (hum>=80)and(hum<=85):
            print('Temperatura estable: ',tem, ' Humedad estable: ',hum)
            estable(tem,hum)
       elif(hum<80):
            print('Temperatura estable: ',tem, ' Humedad baja: ',hum)
            HumBajo(tem,hum)
       elif(hum>85):
            print('Temperatura estable: ',tem, ' Humedad alta: ',hum)
            HumAlto(tem,hum)
    elif (tem>10):
       print('Temperatura baja: ',tem)
       TemBajo(tem,hum)
       if(hum<80):
            print('Temperatura baja: ',tem, ' Humedad baja: ',hum)
            HumBajo(tem,hum)
       elif(hum>85):
            print('Temperatura baja: ',tem, ' Humedad alta: ',hum)
            HumAlto(tem,hum)
    elif (tem<25):
       print('Temperatura alta: ',tem)
       TemAlto(tem,hum)
       if(hum<80):
            print('Temperatura alta: ',tem, ' Humedad baja: ',hum)
            HumBajo(tem,hum)
       elif(hum>85):
            print('Temperatura alta: ',tem, 'Humedad alta: ',hum)
            HumAlto(tem,hum)
    else:
        estable(tem,hum)
