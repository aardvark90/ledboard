
# Test a panel of neopixel LEDS connected in a serial snake
# Works on a 'raspberry pi zero w'. Other models of pi may not work due to the stringent neopixel hardware timing requirements
# Each neopixel package has a Red,Green and Blue LED ...

import board
import neopixel
import time
import random

#total number of LEDS in snake, eg 200 LEDS in a 20x10 array
NUMBER_OF_LEDS = 200

#raspberry pi GPIO 18 connected to the data pin of the first neopixel
pixels = neopixel.NeoPixel(board.D18, NUMBER_OF_LEDS)

#Define RGB intensity
#Dim LEDs
r = [4,0,0]
g = [0,4,0]
b = [0,0,4]
#Bright LEDs!
#r = [128,0,0]
#g = [0,160,0]
#b = [0,0,192]

# an array of two frames of 20x5 LEDs
led_list =[ [\
r,r,r,g,g,g,b,b,b,b,b,b,g,g,g,r,r,r,b,b,\
r,r,r,g,g,g,b,b,b,b,b,b,g,g,g,r,r,r,b,b,\
r,r,r,g,g,g,b,b,b,b,b,b,g,g,g,r,r,r,b,b,\
r,r,r,g,g,g,b,b,b,b,b,b,g,g,g,r,r,r,b,b,\
r,r,r,g,g,g,b,b,b,b,b,b,g,g,g,r,r,r,b,b,\
],\
[\
g,g,g,g,g,r,r,r,r,r,b,b,b,b,b,r,r,r,r,r,\
g,g,g,g,g,r,r,r,r,r,b,b,b,b,b,r,r,r,r,r,\
g,g,g,g,g,r,r,r,r,r,b,b,b,b,b,r,r,r,r,r,\
g,g,g,g,g,r,r,r,r,r,b,b,b,b,b,r,r,r,r,r,\
g,g,g,g,g,r,r,r,r,r,b,b,b,b,b,r,r,r,r,r,\
]
]

while(1):
    print("clear")    
    pixels.fill((0, 0, 0))
    time.sleep(2)

    print("led array")
    for frame in range (len(led_list)):
        for led in range (len(led_list[frame])):
            pixels[led] = led_list[frame][led]
        time.sleep(2)

    print("three fills")
    pixels.fill((4, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 4, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 4))
    time.sleep(0.5)


