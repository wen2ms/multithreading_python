from concurrent.futures import ThreadPoolExecutor


def square(num):
    return num**2


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    with ThreadPoolExecutor(max_workers=2) as executor:
        print(list(executor.map(square, nums)))

        futures = [executor.submit(square, num) for num in nums]
        print([future.result() for future in futures])
