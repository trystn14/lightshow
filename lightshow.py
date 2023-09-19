import board
import time
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness=0.2)

'''

Function: sparkle

Description: This function has a background color and then a random neopixel sparkles. 

Parameters: spark_color- color of the sparkle, back_color- color of the background,
    speed- this is the speed that the sparkles sparkle, num_sparkles- how many sparkles.

Return value: none.

'''
def sparkle(spark_color = [255, 255, 255], back_color = [0, 0, 0], speed = 0.05, num_sparkles = 1):
    for i in range(50):
        np.fill(back_color)
        for j in range(num_sparkles):
            rand_int = random.randrange(0, 30)
            np[rand_int] = spark_color
        np.show()
        time.sleep(speed)
        np[rand_int] = back_color
        np.show()
'''

Function: fade_out

Description: this function fades out with the color.

Parameters: color- what color fades out, speed- how fast the color fades out.

Return value: this function prints the values of red, green, and blue.

'''
def fade_out(color, speed = 1):
    if speed <= 0:
        speed = 1
    red_inc = color[0] / 256.0
    green_inc = color[1] / 256.0
    blue_inc = color[2] / 256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (red_inc * i))
        color1[1] = int (color[1] - (green_inc * i))
        color1[2] = int (color[2] - (blue_inc * i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: fade_in

Description: this function fades in with the color.

Parameters: color- what color fades in, speed- how fast the color fades in.

Return value: this function prints the values of red, green, and blue.

'''
def fade_in(color, speed=1):
    if speed <= 0:
        speed = 1
    red_inc = color[0] / 256.0
    green_inc = color[1] / 256.0
    blue_inc = color[2] / 256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (red_inc * i)
        color1[1] = int (green_inc * i)
        color1[2] = int (blue_inc * i)
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: chase

Description: this function has 2 pixels of one color that follow each other around the strip.

Parameters: chase_color- this sets the color of the 2 pixels, back_color- this sets the one pixel in between the chase,
speed- this is how fast the pixels chase each other.

Return value: none.

'''      
def chase(chase_color = [255, 255, 255], back_color = [0, 0, 0], speed = 0.01):
    for j in range(30):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = chase_color
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = back_color
            time.sleep(speed)

while True:
    #this section is fading in and out between 4 different colors. it loops twice. 
    for i in range(2):
        fade_in([255, 0, 0], 0.005)
        time.sleep(1.5)
        fade_out([255, 255, 255], 0.009)
        fade_in([176, 88, 131], 0.009)
        time.sleep(1)
        fade_out([91, 214, 220], 0.005)
    #this section fades into the color and then sparkles. There is two different color variations. 
    fade_in([255, 0, 0], 0.005)
    sparkle([91, 214, 220], [255, 0, 0], 0.05, 6)
    fade_out([255, 0, 0], 0.009)
    fade_in([255, 255, 255], 0.005)
    sparkle([176, 88, 131], [255, 255, 255])
    fade_out([176, 88, 131], 0.003)
    time.sleep(1)
    #this section uses alternating colors from previous to chase at different speeds. 
    chase([255, 255, 255], [255, 0, 0])
    chase([255, 0, 0], [255, 255, 255], 0.004)
    time.sleep(0.05)
    for i in range(2):
        chase([91, 214, 220], [176, 88, 131], 0.003)
    chase([176, 88, 131], [91, 214, 220])
    #this is the finale that looks like fireworks. 
    sparkle()
    time.sleep(2)
