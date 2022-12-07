from machine import Pin
import time


def debug00():
    a = Pin(15, Pin.OUT)
    b = Pin(2, Pin.OUT)
    c = Pin(4, Pin.OUT)
    d = Pin(16, Pin.OUT)

    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)

    delay_time_ms = 2

    while True:
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)


def init_machinery(lst):
    for each in lst:
        each.value(0)
    time.sleep(0.002)


def debug01():
    pins = [
        Pin(15, Pin.OUT),  # IN1
        Pin(2, Pin.OUT),  # IN2
        Pin(4, Pin.OUT),  # IN3
        Pin(16, Pin.OUT)  # IN4
    ]
    sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    init_machinery(pins)

    while True:
        for step in sequence:
            for i in range(4):
                pins[i].value(step[i])
            time.sleep(0.002)


def rotate_pcw1():
    a = Pin(15, Pin.OUT)
    b = Pin(2, Pin.OUT)
    c = Pin(4, Pin.OUT)
    d = Pin(16, Pin.OUT)

    def setup():
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)

    setup()
    delay_time_ms = 2

    for i in range(256):  # 180 degree
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)

    setup()


def rotate_ncw():
    a = Pin(15, Pin.OUT)
    b = Pin(2, Pin.OUT)
    c = Pin(4, Pin.OUT)
    d = Pin(16, Pin.OUT)

    def setup():
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)

    setup()
    delay_time_ms = 2

    for i in range(128):
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

    setup()


def rotate_pcw2():
    a = Pin(15, Pin.OUT)
    b = Pin(2, Pin.OUT)
    c = Pin(4, Pin.OUT)
    d = Pin(16, Pin.OUT)

    def setup():
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)

    setup()
    delay_time_ms = 2

    for i in range(256):  # 180 degree
        a.value(1)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(1)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)

        a.value(0)
        b.value(0)
        c.value(1)
        d.value(1)
        time.sleep_ms(delay_time_ms)

        a.value(1)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)

    setup()


def main00():
    ts0 = time.time()
    rotate_pcw2()
    ts1 = time.time()
    print(f"{ts1 - ts0}")
    time.sleep(3)
    ts2 = time.time()
    rotate_pcw1()
    ts3 = time.time()
    print(f"{ts3 - ts2}")


STEP_MOTOR_A_PIN = Pin(15, Pin.OUT)  # 橙色
STEP_MOTOR_B_PIN = Pin(2, Pin.OUT)  # 黄色
STEP_MOTOR_C_PIN = Pin(4, Pin.OUT)  # 绿色
STEP_MOTOR_D_PIN = Pin(16, Pin.OUT)  # 蓝色

# 设置步进电机公共端为高电平
STEP_MOTOR_A_PIN.value(0)
STEP_MOTOR_B_PIN.value(0)
STEP_MOTOR_C_PIN.value(0)
STEP_MOTOR_D_PIN.value(0)

STEP_MOTOR_DIRE_FOREWARD = 1  # 步进电机正向转：顺时针
STEP_MOTOR_DIRE_ROLLBACK = -1  # 步进电机正向转：逆时针

STEP_MOTOR_SPEED = 5  # 设置步进电机转动的速度。这个值不能设置太小，否则电机来不及响应


# ========================================================================
# 简述: 步进电机驱动
# 参数: dire：步进电机方向   speed：步进电机转速
# 返回: 无
# 详述:
# ========================================================================
def step_motor_drive(dire, speed):
    if dire == 1:
        step_motor_foreward(speed)
    elif dire == -1:
        step_motor_rollback(speed)
    else:
        print("print input right value!")


# ========================================================================
# 简述: 步进电机停止
# 参数: 无
# 返回: 无
# 详述: （ULN2003有反向功能）
# ========================================================================
def step_motor_stop():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机正转
# 参数: 无
# 返回: 无
# 详述: 顺时针转
# ========================================================================
def step_motor_foreward(speed):
    MotorStepCount = 0
    for i in range(0, 1024):
        if MotorStepCount > 7:
            MotorStepCount = 0
        step_motor_foreward_output(MotorStepCount)
        time.sleep_ms(speed);
        MotorStepCount = MotorStepCount + 1


# ========================================================================
# 简述: 步进电机反转
# 参数: 无
# 返回: 无
# 详述: 逆时针转
# ========================================================================
def step_motor_rollback(speed):
    MotorStepCount = 0
    for i in range(0, 1024):
        if (MotorStepCount) > 7:
            MotorStepCount = 0
        step_motor_rollback_output(MotorStepCount)
        time.sleep_ms(speed)
        MotorStepCount = MotorStepCount + 1

    # ========================================================================


# 简述: 步进电机正向输出
# 参数: 无
# 返回: 无
# 详述:
# ========================================================================
def step_motor_foreward_output(step):
    if step == 0:
        step_motor_a_output()
    elif step == 1:
        step_motor_ab_output()
    elif step == 2:
        step_motor_b_output()
    elif step == 3:
        step_motor_bc_output()
    elif step == 4:
        step_motor_c_output()
    elif step == 5:
        step_motor_cd_output()
    elif step == 6:
        step_motor_d_output()
    elif step == 7:
        step_motor_da_output()
    else:
        print("Please input right value")


# ========================================================================
# 简述: 步进电机反向输出
# 参数: 无
# 返回: 无
# 详述:
# ========================================================================
def step_motor_rollback_output(step):
    if step == 0:
        step_motor_a_output()
    elif step == 1:
        step_motor_da_output()
    elif step == 2:
        step_motor_d_output()
    elif step == 3:
        step_motor_cd_output()
    elif step == 4:
        step_motor_c_output()
    elif step == 5:
        step_motor_bc_output()
    elif step == 6:
        step_motor_b_output()
    elif step == 7:
        step_motor_ab_output()
    else:
        print("Please input right value")


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机A相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_a_output():
    STEP_MOTOR_A_PIN.value(1)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机AB相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_ab_output():
    STEP_MOTOR_A_PIN.value(1)
    STEP_MOTOR_B_PIN.value(1)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机B相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_b_output():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(1)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机BC相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_bc_output():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(1)
    STEP_MOTOR_C_PIN.value(1)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机C相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_c_output():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(1)
    STEP_MOTOR_D_PIN.value(0)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机CD相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_cd_output():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(1)
    STEP_MOTOR_D_PIN.value(1)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机D相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_d_output():
    STEP_MOTOR_A_PIN.value(0)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(1)


# ========================================================================
# 简述: 步进电机引脚控制
# 参数: 无
# 返回: 无
# 详述: 步进电机DA相输出（ULN2003有反向功能）
# ========================================================================
def step_motor_da_output():
    STEP_MOTOR_A_PIN.value(1)
    STEP_MOTOR_B_PIN.value(0)
    STEP_MOTOR_C_PIN.value(0)
    STEP_MOTOR_D_PIN.value(1)


def main():
    step_motor_drive(1, 5)  # 正向（顺时针）转动，每个相位间隔时间5ms
    step_motor_drive(-1, 5)  # 反向（逆时针）转动，每个相位间隔时间5ms
    step_motor_stop()


if __name__ == '__main__':
    main()
