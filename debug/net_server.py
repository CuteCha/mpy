# -*- coding: utf-8 -*-
import socket
import time


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("192.168.2.105", 7788)

    while True:
        print("=" * 36)
        start = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
        msg = input("content:")
        client_socket.sendto(msg.encode("utf-8"), server_address)
        now = time.time()
        run_time = now - start
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
        print(f"run_time: {run_time} seconds\n")


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("0.0.0.0", 9090)
    server_socket.bind(server_address)
    server_socket.settimeout(10)

    while True:
        try:
            now = time.time()
            print("=" * 36)
            receive_data, client_info = server_socket.recvfrom(1024)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
            print(f"from:{client_info},content:{receive_data.decode()}\n")
        except socket.timeout:
            print("receiving ......")


if __name__ == '__main__':
    # client()
    server()
