from multiprocessing import Process
import os


def print_numbers():
    print(f"Process ID: {os.getpid()} - Numbers:", list(range(5)))


def print_letters():
    print(f"Process ID: {os.getpid()} - Letters:", list("ABCDE"))


if __name__ == "__main__":
    # Create processes
    process1 = Process(target=print_numbers)
    process2 = Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to finish
    process1.join()
    process2.join()

    print("Both processes have finished execution.")
