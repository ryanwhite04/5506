
from gpiozero import Button, LED
from time import time, sleep
from random import randint

def main():
    led = LED(17)
    btn = Button(4)
    while True:
        sleep(randint(1,10))
        led.on()
        start = time()
        btn.wait_for_press()
        end = time()
        led.off()
        print(end - start)

if __name__ == '__main__': main()