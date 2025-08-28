# Generator is a simple way of creating iterator

def count_up_to(n):
    """Generator that counts from 1 to n."""
    count = 1
    while count <= n:
        yield count # Yield pauses the function and returns the value
        count += 1 

# Example usage:
for number in count_up_to(5):
    print(number)



# Iterator version of count_up_to
class CountUpTo:
    """Iterator that counts from 1 to n."""
    def __init__(self, n):
        self.n = n
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            current = self.count
            self.count += 1
            return current
        else:
            raise StopIteration



# Example usage:
for number in CountUpTo(5):
    print(number)