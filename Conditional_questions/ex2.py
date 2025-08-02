# Movie Ticket Pricing
#Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("enter your age : "))

day = "wednesdsy"

if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesdsy":
    price -= 2
print("Ticket price for you is $",price)    

          
    
