import math
import random
def colourChange(colour,time):
    min = 0
    max = 255
    #print(time)
    colour0 =0# abs(255 * math.sin(2*math.pi*time)) #* math.sin(time*2*math.pi + random.random()*255))
    colour1 = abs(255 * math.sin(2*math.pi*time))
    colour2 = 0#abs(255 * math.sin(2*math.pi*time))#* math.sin(time*2*math.pi + random.random()*255))

    return colour0, colour1 , colour2
