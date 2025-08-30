# 1. What is a decorator?

# A decorator in Python is just a function that:
# Takes another function as input (func).
# Returns a new function that adds extra behavior (without modifying the original function’s code).
# They are often used for logging, access control, instrumentation, and caching.


import time

def cal_square(numbers):
    start = time.time()
    result = []
    for n in numbers:
        result.append(n * n)
    end = time.time()
    print("Time taken to calculate squares: " + str((end - start) * 1000) + " milli seconds")
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for n in numbers:
        result.append(n * n * n)
    end = time.time()
    print("Time taken to calculate cubes: " + str((end - start) * 1000) + " milli seconds")
    return result


array = range(1, 11)
print(cal_square(array))
print(calc_cube(array))
