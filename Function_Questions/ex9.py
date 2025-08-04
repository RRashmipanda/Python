# Generator Function with yield
# Write a generator function that yields even numbers up to a specified limit.


def even_generator(limit):
    for i in range(2, limit + 1, 2):  # range(start, stop, step).It starts from 2, goes up to limit + 1, with a step of 2.
                                      # So for limit = 10, the values of i will be: 2, 4, 6, 8, 10                         
        yield i     # 	Instead of returning all values at once, it pauses and returns one value at a time.
 


for num in even_generator(10):   # It runs a loop that fetches each yielded value from the generator one by one and assigns it to num.
    print(num)