import threading
import time


def working_1():
    global shared_data, lock

    for _ in range(10):
        lock.acquire()

        shared_data += 1

        print(f"worker_1, shared_data = {shared_data}")

        time.sleep(0.1)

        lock.release()


def working_2():
    global shared_data, lock

    for _ in range(10):
        lock.acquire()

        shared_data += 5

        print(f"worker_2, shared_data = {shared_data}")

        time.sleep(0.1)

        lock.release()


if __name__ == "__main__":
    shared_data = 0

    lock = threading.Lock()

    worker_1 = threading.Thread(target=working_1)

    worker_2 = threading.Thread(target=working_2)

    worker_1.start()

    worker_2.start()

    worker_1.join()

    worker_2.join()
