import threading
from time import sleep


def working():
    sleep(2)

    print(f"This is a added thread, ID is {threading.current_thread()}")


def main():
    # added_thread = threading.Thread(target=working, daemon=True)
    added_thread = threading.Thread(target=working)

    added_thread.start()

    print(threading.active_count())

    print(threading.enumerate())

    print(threading.current_thread())


if __name__ == "__main__":
    main()
