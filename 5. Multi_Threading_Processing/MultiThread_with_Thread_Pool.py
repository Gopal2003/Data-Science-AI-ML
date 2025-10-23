from concurrent.futures import ThreadPoolExecutor
import time



def print_number(number):
     time.sleep(1)
     return f"Number :{number}"


numbers = [1,2,3,4,5]

t = time.time()
with ThreadPoolExecutor(max_workers=2) as executor:
     results = executor.map(print_number,numbers)


total_time_taken = time.time() - t
print(total_time_taken)

for result in results:
     print(result)
