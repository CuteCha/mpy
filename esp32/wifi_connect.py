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


if __name__ == '__main__':
    do_connect()
