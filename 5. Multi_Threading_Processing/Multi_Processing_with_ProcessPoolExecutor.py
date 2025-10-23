from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
    time.sleep(1)
    return f"Square: {number * number}"

numbers = [1,2,3,4,5]

t = time.time()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)

    Total_time = time.time() - t
    print(Total_time)