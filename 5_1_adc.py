import RPi.GPIO as gp
import time

def dec_to_bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

def adc():
    for i in range(256):
        bin_i = dec_to_bin(i)
        gp.output(dac, bin_i)
        time.sleep(0.007)
        c = gp.input(comp)
        if c == 1:
            return i
    return 255

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
tr = 13
gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)
gp.setup(tr, gp.OUT, initial = 1)
gp.setup(comp, gp.IN)

try:
    while True:
        num = adc()
        print(f'{num*3.3/256}v')
        time.sleep(0.1)
finally:
    gp.output(dac, 0)
    gp.output(tr, 0)
    gp.cleanup()