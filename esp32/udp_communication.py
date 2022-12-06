import socket
import time
import network
import machine


def connect_wifi():
    ssid = "wifi_name"
    key = "wifi_key"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            time.sleep(0.1)
            pass
    print(f"network config: {wlan.ifconfig()}")


def create_udp_socket():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 7788))

    return udp_socket


def recv_signal_from_pc():
    connect_wifi()
    udp_socket = create_udp_socket()
    led = machine.Pin(2, machine.Pin.OUT)
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)

        try:
            recv_data_str = recv_data.decode("utf-8")
            print(f"recv_data: {recv_data_str}; from: {sender_info}")
            if recv_data_str == "1":
                print("led light on")
                led.value(1)
            elif recv_data_str == "0":
                print("led light off")
                led.value(0)
        except Exception as ret:
            print("error:", ret)


def send_signal_to_pc():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('192.168.2.104', 9090)
    while True:
        print("=" * 36)
        msg = input("content:")
        client_socket.sendto(msg.encode("utf-8"), dest_addr)


if __name__ == '__main__':
    # recv_signal_from_pc()
    send_signal_to_pc()
