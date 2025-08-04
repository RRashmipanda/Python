# Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# **kwargs allows a function to accept any number of keyword arguments. syntax - def function_name(**kwargs):

# It collects them into a dictionary (dict), where:
     # keys are the argument names
     # values are the values passed

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")