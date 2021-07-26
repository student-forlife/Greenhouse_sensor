import machine
from machine import ADC
from machine import Pin
import time

# sensor connected to P16 and P14
# set up pin mode to input
lightPin = Pin('P16', mode=Pin.IN)
tempPin = Pin('P14')

# create an ADC object, bits=10 means range 0-1024 the lower value the less light detected
adc = machine.ADC()
# create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
lpin = adc.channel(attn=ADC.ATTN_11DB, pin=lightPin)
tpin = adc.channel(pin=tempPin)

while True:
    # Light sensor
    light = lpin() # read an analog value
    # Sending to pybytes in channel 3
    pybytes.send_signal(3, light)
    print("Value", light)
    
    # Temperature sensor
    millivolts = tpin.voltage()
    celsius = (millivolts - 500.0) / 10.0
    
    #Sending to pybytes in channel 1
    pybytes.send_signal(1, celsius)
    print("Value {}".format(celsius))
    
    time.sleep(1800)  # wait 30 min
