import threading
from queue import Queue


def working(data, results_queue):
    print(f"worker id = {threading.current_thread()}")

    for i in range(len(data)):
        data[i] = data[i] ** 2

    results_queue.put(data)


def main():
    results_queue = Queue()

    threads = []

    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    for i in range(len(data)):
        # args must be tuple
        worker = threading.Thread(target=working, args=(data[i], results_queue))

        worker.start()

        threads.append(worker)

    for thread in threads:
        thread.join()

    results_list = []
    while not results_queue.empty():
        results_list.append(results_queue.get())

    print(results_list)


if __name__ == "__main__":
    main()
