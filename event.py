import time
from threading import Event, Thread

event = Event()


def bus():
    print("Bus is comming")
    time.sleep(3)
    print("Bus arrived")
    event.set()


def passenger(name):
    print(name, "is waiting")
    event.wait()
    print(name, "Go")


if __name__ == "__main__":
    processes = []
    process = Thread(target=bus)
    process.start()
    processes.append(process)

    for i in range(10):
        process = Thread(
            target=passenger,
            args=(f"passenger{i}",),
        )
        process.start()
        processes.append(process)
