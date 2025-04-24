import RPi.GPIO as gp
import time

def dec_to_bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

def adc():
    l = list()
    for i in range(8):
        l.append(1)
        gp.output(dac[0:int(i + 1)], l)
        time.sleep(0.01)
        c = gp.input(comp)
        if c == 1:
            c = 0
        else:
            c = 1
        l[i] = c
    num = ''
    for i in l:
        num += str(i)
    gp.output(dac, 0)
    return int(num, 2)
        

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 19]
comp = 14
tr = 13
gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)
gp.setup(leds, gp.OUT)
gp.setup(tr, gp.OUT, initial = 1)
gp.setup(comp, gp.IN)

try:
    while True:
        num = adc()
        print(f'{num*3.3/256}v')
        num_leds = min(int(num/255*8), 8)
        fire = [0]* 8
        for i in range(num_leds):
            fire[7 - i] = 1
        gp.output(leds, 0)
        gp.output(leds, fire)
        time.sleep(0.1)
finally:
    gp.output(dac, 0)
    gp.output(tr, 0)
    gp.cleanup()