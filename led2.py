import board
import neopixel
import time

NUM_LEDS=50
COLOR = (90,30,10)
COLOR2 = (30,90,10)
pixel = neopixel.NeoPixel(board.A1, 51, pixel_order=neopixel.GRB)
x=range(NUM_LEDS)
y=range(NUM_LEDS,1,-1)
while True:


    for a in x:
        if a > 1:
            pixel[a-1] = (0,0,0)
            pixel[a] = COLOR
            pixel[50-a] = (0,0,0)
            pixel[49-a] = COLOR2
        time.sleep(.05)
    pixel[49] = (0, 0, 0)
    pixel[0] = (0,0,0)