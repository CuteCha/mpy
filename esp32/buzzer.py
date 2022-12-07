from machine import Pin
from machine import PWM
from time import sleep_ms


def active_buzzer():
    p15 = Pin(15, Pin.OUT)
    for i in range(10):
        p15.value(1)  # off
        sleep_ms(200)
        p15.value(0)  # on
        sleep_ms(200)

    p15.value(1)  # shut


class BUZZER:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))

    def play(self, melodies, wait, duty):
        for note in melodies:
            print("note:{}".format(note))
            if note:
                self.pwm.freq(note)
            self.pwm.duty(duty)
            sleep_ms(wait)
        # 暂停PWM，将占空比设置为0
        self.pwm.duty(0)


def passive_buzzer():
    # 音符与对应的的频率
    B0 = 31
    C1 = 33
    CS1 = 35
    D1 = 37
    DS1 = 39
    E1 = 41
    F1 = 44
    FS1 = 46
    G1 = 49
    GS1 = 52
    A1 = 55
    AS1 = 58
    B1 = 62
    C2 = 65
    CS2 = 69
    D2 = 73
    DS2 = 78
    E2 = 82
    F2 = 87
    FS2 = 93
    G2 = 98
    GS2 = 104
    A2 = 110
    AS2 = 117
    B2 = 123
    C3 = 131
    CS3 = 139
    D3 = 147
    DS3 = 156
    E3 = 165
    F3 = 175
    FS3 = 185
    G3 = 196
    GS3 = 208
    A3 = 220
    AS3 = 233
    B3 = 247
    C4 = 262
    CS4 = 277
    D4 = 294
    DS4 = 311
    E4 = 330
    F4 = 349
    FS4 = 370
    G4 = 392
    GS4 = 415
    A4 = 440
    AS4 = 466
    B4 = 494
    C5 = 523
    CS5 = 554
    D5 = 587
    DS5 = 622
    E5 = 659
    F5 = 698
    FS5 = 740
    G5 = 784
    GS5 = 831
    A5 = 880
    AS5 = 932
    B5 = 988
    C6 = 1047
    CS6 = 1109
    D6 = 1175
    DS6 = 1245
    E6 = 1319
    F6 = 1397
    FS6 = 1480
    G6 = 1568
    GS6 = 1661
    A6 = 1760
    AS6 = 1865
    B6 = 1976
    C7 = 2093
    CS7 = 2217
    D7 = 2349
    DS7 = 2489
    E7 = 2637
    F7 = 2794
    FS7 = 2960
    G7 = 3136
    GS7 = 3322
    A7 = 3520
    AS7 = 3729
    B7 = 3951
    C8 = 4186
    CS8 = 4435
    D8 = 4699
    DS8 = 4978

    jingle = [
        E7, E7, E7, 0,
        E7, E7, E7, 0,
        E7, G7, C7, D7, E7, 0,
        F7, F7, F7, F7, F7, E7, E7, E7, E7, D7, D7, E7, D7, 0, G7, 0,
        E7, E7, E7, 0,
        E7, E7, E7, 0,
        E7, G7, C7, D7, E7, 0,
        F7, F7, F7, F7, F7, E7, E7, E7, G7, G7, F7, D7, C7, 0
    ]

    buzzer = BUZZER(15)
    buzzer.play(jingle, 250, 512)
    sleep_ms(1000)


def main():
    # active_buzzer()
    passive_buzzer()


if __name__ == '__main__':
    main()
