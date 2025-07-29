# Tuple is a list of values grouped together

point = (1, 2, 3, 4, 5)
print(point)
# Accessing elements in a tuple
print(point[3])

# difference between tuple and list
# Tuples are immutable, meaning they cannot be changed after creation
# Lists are mutable, meaning they can be changed after creation
point[0] = 10  # This will raise an error because tuples cannot be modified

#  List:All values have similar meaning Tuple: All values have different meaning
# Example of a tuple with different types of values
person = ("John", 30, "Engineer")