# Store monthly expenses in a list and find out total expenses for all months

exp = [1200, 1500, 1300, 1600, 1400, 1700, 1800, 1900, 2000, 2100, 2200, 2300]

total = 0
for item in exp:
    total = total+item
print("Total expenses for the year: $", total)   

for i in range(len(exp)):
    print("Month : ", (i+1), "Expense: ", exp[i])
    total = total + exp[i]
print("Total expenses for the year: $", total)


print number 1 to 100 By  range function
for i in range(1,101):
    print(i)
    print(i*i)


# break statements
# Find the key in a list of locations using a for loop and break statement
key_location ="chair"
locations = ["table", "sofa", "bed", "chair","desk"]
for i in locations:
    if i == key_location:
        print("Key found at location:", i)
        break
    else:
        print("Key not found at location:", i)  
        
# continue statements
# Print even numbers from 1 to 20 using continue statement
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)          
 

 # While loop
 # printing 1 to 10 using while loop
i =1
while i<=10:
    print(i)
    i = i+1 