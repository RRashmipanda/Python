item1= "Bread"
item2= "Milk"
item3= "Eggs"

items = [item1, item2, item3]
print("Shopping List:", items)
print (items[0])
items[0] = 'Butter'
print("Updated Shopping List:", items)

print (items[0:2])
print(items[-1])  # Last item in the list
print(len(items))  # Length of the list

items.append("Cheese")  # Adding an item to the end of the list
print("After adding Cheese:", items)

items.insert(1, "Yogurt")  # Inserting an item at index 1
print("After inserting Yogurt at index 1:", items)


items.remove("Milk")  # Removing an item by value
print("After removing Milk:", items)

# join two lists
foods = ["Pizza", "Pasta"]
final_list = items + foods
print("Final List after joining with foods:", final_list)

# foods+"Salad"  # This does not change the original list

# Sorting the list
final_list.sort()
print("Sorted Final List:", final_list)

# Reversing the list
final_list.reverse()
print("Reversed Final List:", final_list)

# Slicing the list
sliced_list = final_list[1:4]  # Slicing from index 1 to 3
print("Sliced List (index 1 to 3):", sliced_list)

print("final list:", final_list)

# in operator
"Pizza" in final_list  # Returns True if "Pizza" is in final_list

# Checking if an item exists in the list
if "Pasta" in final_list:
    print("Pasta is in the final list.")
   