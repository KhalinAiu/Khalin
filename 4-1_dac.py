import RPi.GPIO as GPIO
def dec_to_bin(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]

dac = [8, 11, 7 ,1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        s = input('Введи целое число от 0 до 255: ')
        if s == 'q':
            break
        if int(s) < 0:
            print('Вы ввели число меньше 0')
            continue
        if int(s) > 255:
            print('Вы ввели число больше 255')
            continue
        GPIO.output(dac, dec_to_bin(int(s)))
        print(f"Предполагаемое значение н авыходе {3.3 * int(s) / 256}В")

except ValueError:
    print('Invalid value')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()