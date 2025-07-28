# enter a number and check if it is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")    

# operators
4 == 4  # This is a comparison operator, it checks if the two values are equal
4 != 5  # This checks if 4 is not equal to 5
4 != 4 # This checks if 4 is not equal to 4

4 < 5  # This checks if 4 is less than 5
4 > 3  # This checks if 4 is greater than 3
4 <= 4  # This checks if 4 is less than or equal to 4
4 >= 3  # This checks if 4 is greater than or equal to 3

# Logical operators
# and, or, not  
3>2 and 4>3  # This checks if both conditions are true
3>2 or 4<3  # This checks if at least one condition is true

# not operator
not (3 > 2)  # This negates the condition, so it returns False


# wap that asks user to enter dish name and it should print which cuisine is that dish belongs to
indian_dishes = ["Biryani", "Paneer Tikka", "Samosa"]
italian_dishes = ["Pizza", "Pasta", "Lasagna"]
chinise_dishes = ["Noodles", "Spring Rolls", "Dumplings"]

dish = input("Enter a dish name: ")

if dish in indian_dishes:
    print("Indian Cuisine")
elif dish in italian_dishes:
    print("Italian Cuisine")
elif dish in chinise_dishes:
    print("Chinese Cuisine") 
else:
     print("Cuisine not found for the dish:", dish)       
