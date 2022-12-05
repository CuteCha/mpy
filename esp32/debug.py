import machine
import sys


def main(argv):
    print("hello esp32")
    pin2 = machine.Pin(2, machine.Pin.OUT)
    if len(argv) <= 1:
        print("no argv")
    if argv[1] == "1":
        pin2.value(1)
    elif argv[1] == "0":
        pin2.value(0)
    else:
        print("unknown argv")


if __name__ == '__main__':
    main(sys.argv)
