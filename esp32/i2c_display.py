import time
from machine import SoftI2C, Pin
from esp32_i2c_1602lcd import I2cLcd


def debug(lcd):
    for i in range(21):
        lcd.clear()
        lcd.putstr(f"loading...{i}\ncdy")
        time.sleep(1)


def add_alg(lcd):
    for i in range(1, 10):
        for j in range(1, 10):
            lcd.clear()
            lcd.putstr(f"{i} + {j} = {i + j}")
            time.sleep(5)


def main():
    DEFAULT_I2C_ADDR = 0x27
    i2c = SoftI2C(sda=Pin(15), scl=Pin(2), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    # debug(lcd)
    add_alg(lcd)


if __name__ == '__main__':
    main()
