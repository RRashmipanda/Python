# Recursive Function
# Create a recursive function to calculate the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # This is the recursive case.The function calls itself with a smaller value until it reaches n == 0.


    
number= int(input("Enter number : "))
factorial = factorial(number)
print(factorial)
