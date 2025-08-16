# exception means error occurred in the program
# exception handling is a way to handle errors gracefully

x = input("Enter a number 1: ")
y=input("Enter a number 2: ")

try:
    z=x / int(y)  
# except Exception as e:
#     print('exception occured:', e)
#     z=None
except Exception as e:
    print("exception type is ", type(e).__name__)
    z = None
print("Result:", z) 


