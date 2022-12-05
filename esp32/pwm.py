from machine import Pin, PWM
import time


def debug():
    led = PWM(Pin(2))
    led.freq(1000)
    led.duty(100)


def main():
    led = PWM(Pin(2))
    led.freq(1000)

    while True:
        for i in range(0, 1024):
            led.duty(i)
            time.sleep(0.001)

        for i in range(1023, -1, -1):
            led.duty(i)
            time.sleep(0.001)


if __name__ == '__main__':
    main()
