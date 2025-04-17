import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
voltage = GPIO.PWM(24, 1000)
voltage.start(0)
try:
    while True:
        t = int(input())
        voltage.ChangeDutyCycle(t)
        print(f'Предпологаемое напряжение {3.3 * t /100 :.3}')
        

finally:
    GPIO.output(24, 0)
    GPIO.cleanup()
