# Doucument string is nothing but way to document your functions, classes, modules, etc.\


""" this function is used to sum two numbers
    it takes two arguments a and b and returns their sum"""
total = 0
def sum(a,b):
    total = a+b
    print("total in inside function",total)
    return total

n = sum(6,4) 
print(n)

print("total in outside function",total)  