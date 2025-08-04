# Function with *args
# Write a function that takes variable number of arguments and returns their sum.


def sum_all(*args):    # *args allows a function to accept any number of positional arguments.
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3,4))  # it's just using Python's built-in sum() function.