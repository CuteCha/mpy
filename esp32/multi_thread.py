import _thread
import time


def func01(*args, **kwargs):
    for i in range(3):
        print("1")
        time.sleep(1)


def func02(*args, **kwargs):
    for i in range(3):
        print("2")
        time.sleep(1)


def main():
    thread_1 = _thread.start_new_thread(func01, (1,))
    thread_2 = _thread.start_new_thread(func02, (2,))



if __name__ == '__main__':
    main()
