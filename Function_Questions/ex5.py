# Default Parameter Value
# Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"):  # name = "User" sets "User" as the default value.
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())