# Benifits of generators
# 1 Dont need to define __iter__ and __next__ methods
# 2 Memory efficient - dont need to store all values in memory
# 3 dont need to raise StopIteration exception

# fibonacci sequence using generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b # a = b, b= a + b
for f in fib():
    if f > 100: # Limit output to numbers less than or equal to 100
        break
    print(f)        
 

#  Python first evaluates the right-hand side (RHS) completely,
# then assigns values to the left-hand side (LHS).

# Suppose a = 0, b = 1

# RHS = (b, a + b) → (1, 0 + 1) → (1, 1)
# LHS = (a, b)

# So a = 1
# And b = 1


