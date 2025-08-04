# Polymorphism in Functions
# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(p1, p2):
    return p1 * p2


print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, 'a'))

# In Python, multiplying a string with an integer repeats the string that many times. 
# 'a' * 5 == 5 * 'a'  # both yield 'aaaaa'
