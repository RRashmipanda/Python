total = 0  
def sum(a,b=0): # inside a function argument when you assign specific value to an argument it is called default argument
    total = a+b
    print("total in inside function",total)
    return total

n = sum(6,4) # when you already pass here thrn function will not use default value
print(n)

print("total in outside function",total)  