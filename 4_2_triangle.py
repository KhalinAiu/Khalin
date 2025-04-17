import RPi.GPIO as GPIO
import time

def dec_to_bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]

dac = [8, 11, 7 ,1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period = int(input())
    k = 1
    num = 0
    while True:
        
        GPIO.output(dac, dec_to_bin(num))
        time.sleep(period/510)
        num += k
        if num == 256 or num == -1:
            k = k * (-1)
            num += k

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()