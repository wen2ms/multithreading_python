import threading
import time
from queue import Queue


def working(data, results_queue):
    print(f"worker id = {threading.current_thread()}")

    data_sum = sum(data)

    results_queue.put(data_sum)


def multithreading(data):
    results_queue = Queue()

    threads = []

    for _ in range(4):
        worker = threading.Thread(target=working, args=(data, results_queue))

        worker.start()

        threads.append(worker)

    [thread.join() for thread in threads]

    data_sum = 0
    while not results_queue.empty():
        data_sum += results_queue.get()

    print(data_sum)


def normal(data):
    print(sum(data))


if __name__ == "__main__":
    data = list(range(1000000))

    start_time = time.time()

    normal(data * 4)

    print(f"normal time: {time.time() - start_time}")

    start_time = time.time()

    multithreading(data)

    print(f"multithreading time: {time.time() - start_time}")
