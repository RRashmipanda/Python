# sum
total = 0  # global variable
def sum(a,b):
    total = a+b
    print("total in inside function",total)
    return total

n = sum(6,7) # position arguments
# print(n)

# you can pass named arguments like n = sum(b=6,a=7)

print("total in outside function",total)  
