# Decorate ex1
import time

# Decorator to measure execution time
def time_it(func):
    def wrapper(*args, **kwargs): #*args and **kwargs make sure the wrapper can accept any number of arguments
        start = time.time()
        result = func(*args, **kwargs)   # call the actual function
        end = time.time()
        print(f"Time taken to execute '{func.__name__}': {(end - start) * 1000:.4f} milli seconds") #:.4f → format to 4 decimal places.
        return result
    return wrapper


@time_it
def cal_square(numbers):
    return [n * n for n in numbers]


@time_it
def calc_cube(numbers):
    return [n * n * n for n in numbers]


array = range(1, 11)

print("Squares:", cal_square(array))
print("Cubes:", calc_cube(array))


# def wrapper(*args, **kwargs):


# *args → positional arguments (func(1, 2, 3) → args = (1, 2, 3)).
# **kwargs → keyword arguments (func(a=10, b=20) → kwargs = {a:10, b:20}).

# This way, time_it can decorate any function, regardless of its arguments.