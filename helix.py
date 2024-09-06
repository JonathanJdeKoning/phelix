from time import sleep
from math import sin, ceil, floor, cos, tan
import random
time= 0

light = list('@xx==++;;::.-')
dark = light[::-1]

#Variables
sample_speed = 0.175
speed = 40
intensity = 40
slope = -4
rise = 11
thickness = 1
viz = light 
############

while True:
    sleep(1/speed)
    distance = ceil(intensity*sin(time))
    
    width = ceil(abs(distance)/slope+rise)
    char = viz[abs(distance)//(intensity//len(viz)+1)]

    for _ in range(thickness):
        print((distance+intensity)*" ", end = "")
        print(char*width)

    time=round(time+sample_speed, 3)
    if time>sample_speed*107:
        intensity = random.randint(20,60)
        slope = random.randint(2,10)
        rise = random.randint(1,20)
        thickness = random.randint(1,3)
        if random.randint(0,1) == 0:
            viz = light
        else:
            viz = dark
        time = 0
        
"""
DEFAULTS:
sample_speed = 0.175
speed = 20
intensity = 40
slope = -4
rise = 11
vis = light
"""