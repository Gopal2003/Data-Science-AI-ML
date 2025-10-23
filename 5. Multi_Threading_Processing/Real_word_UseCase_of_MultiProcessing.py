import sys
import time
import multiprocessing
import math
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(100000)

#Function to calculate the factorial
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers= [5000,6000,7000,8000]

    start = time.time()

    with multiprocessing.Pool() as executor:
        result = executor.map(compute_factorial,numbers)

    end_time = time.time()
    
    print("Result: ", result)
    print("Total Time taken: ", end_time - start)