import threading
import time

def working_1():
    print(f"worker {threading.current_thread()} start")

    time.sleep(2)

    print(f"worker {threading.current_thread()} finished")

def working_2():
    print(f"worker {threading.current_thread()} start")

    print(f"worker {threading.current_thread()} finished")

def main():
    worker_1 = threading.Thread(target=working_1, name='worker_1')

    worker_2 = threading.Thread(target=working_2, name='worker_2')

    worker_1.start()

    worker_2.start()

    worker_1.join()
    
    worker_2.join()

    print("all threads done")

if __name__ == "__main__":
    main()