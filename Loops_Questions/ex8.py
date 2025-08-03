# Prime Number Checker
# Check if a number is prime.

number = 6

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)

# if number  = 7 That means the loop runs with i = 2, 3, 4, 5, 6 then (7 % i)