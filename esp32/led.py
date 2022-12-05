import machine
import time


def say():
    print("hello esp32 iot")


def main():
    led = machine.Pin(2, machine.Pin.OUT)

    while True:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
