# An iterator is an object in Python that allows you to iterate (loop) through elements one at a time.

# It implements two methods:

# __iter__() → Returns the iterator object itself.
# __next__() → Returns the next element in the sequence.

# A list is an iterable (not an iterator itself)
numbers = [1, 2, 3]

# Get an iterator from the list
it=iter(numbers)

# Use next() to get elements one by one
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# If we go beyond the limit, it raises StopIteration
# print(next(it))  #  StopIteration
print(dir(it))

#iterating through list
for element in [1,2,3]:
    print(element)

#iterating through tuple
for element in (1,2,3):
    print(element)

#iterating through dictionary
for key in {'a':1,'b':2,'c':3}:
    print(key)

#iterating through set
for element in {1,2,3}:
    print(element)

#iterating through string
for char in "123":
    print(char)


# iterating through file
for line in open ("myfile.txt"):
    print(line, end='')