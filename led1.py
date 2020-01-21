import board
import neopixel
import time

NUM_LEDS=50
pixel = neopixel.NeoPixel(board.A1, 51, pixel_order=neopixel.GRB)
x=range(NUM_LEDS)
y=range(NUM_LEDS,1,-1)
while True:


    for a in x:
        if a > 1:
            pixel[a-1] = (0,0,0)
            pixel[a] = (40,30,20)
        time.sleep(.05)
    pixel[50] = (0, 0, 0)
    for b in y:
        if b < 50:
            pixel[b+1]= (0,0,0)
            pixel[b] = (40,30,20)
        time.sleep(.05)
    pixel[1] = (0,0,0)
    pixel[50] = (0,0,0)