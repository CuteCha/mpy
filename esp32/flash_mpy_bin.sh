#!/bin/bash

#install esptool
~/env/anaconda3/bin/pip install esptool
#erase the entire flash # usb: /dev/cu.usbserial-0001
#~/env/anaconda3/bin/esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
~/env/anaconda3/bin/esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash
#From then on program the firmware starting at address 0x1000
#~/env/anaconda3/bin/esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
~/env/anaconda3/bin/esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 460800 write_flash -z 0x1000 ./data/tools/esp32-20220618-v1.19.1.bin
#查看到文件列表
~/env/anaconda3/bin/ampy -d 1 --port /dev/cu.usbserial-0001 --baud 115200 ls
#文件名必须是main.py
~/env/anaconda3/bin/ampy -d 1 --port /dev/cu.usbserial-0001 --baud 115200 put main.py
~/env/anaconda3/bin/ampy -d 1 --port /dev/cu.usbserial-0001 --baud 115200 run main.py
~/env/anaconda3/bin/ampy -d 1 --port /dev/cu.usbserial-0001 --baud 115200 reset
#查看交互式界面
screen

#在REPL执行
exec(open("main.py").read())
