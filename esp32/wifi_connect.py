import network
import time

ssid = "wifi_name"
key = "wifi_key"


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            time.sleep(0.1)
            pass
    print("network config:", wlan.ifconfig())
    print("mac: ", wlan.config("mac"))


def do_access():
    ap = network.WLAN(network.AP_IF)
    ap.config(ssid='ESP-AP')
    ap.config(max_clients=10)
    ap.active(True)


if __name__ == '__main__':
    do_connect()
