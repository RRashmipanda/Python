# List comprehension provides a way to transform one list to another
numbers = [1, 2, 3, 4, 5]
even = [i for i in numbers if i % 2 == 0]
print(even)  

squares = [i * i for i in numbers]
print(squares)


# Set comprehension is similar to list comprehension but creates a set
# Sets automatically handle duplicates

s =set([1,2,3,4,5,2,3])
print(s)

squared_set = {i * i for i in numbers}
print(squared_set)
