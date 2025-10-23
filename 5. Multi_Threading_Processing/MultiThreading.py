import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")


def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


t1 = threading.Thread(target= print_numbers)
t2 = threading.Thread(target= print_letter)

t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

# If i remove t1.join(), the main thread don't wait for the threads t1 and t2 and hence will print the finishted_time since no other code is writte which outputs in terminal.
finished_time = time.time() - t
print(finished_time)
