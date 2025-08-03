# Validate Input
# Keep asking the user for input until they enter a number between 1 and 10.


while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:     # if number >= 1 and number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")

# explain
#  while True:This creates an infinite loop, meaning the loop will keep running forever unless it hits a break statement.   
     