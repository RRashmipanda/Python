# Json is light weight data interchange format compared to xml

# we will write two programs
# 1. to create a address book and write some records to it
# 2. to read the address book 

book = {}

book["Lipun"] = {
    "name": "Lipun",
    "email": "abc@gmail.com",
    "phone": "1234567890",
    "address": "123, Main Street, City"
}
book["John"] = {
    "name": "John", 
    "email": "a@gmail.com",
    "phone": "0987654321",  
    "address": "456, Elm Street, City"
}

import json
s = json.dumps(book)
with open("E:/wvdv coding/Python/11_WorkingWithJson/book.txt", "w") as f:
    f.write(s)  

# Now we will read the address book from the file
with open("E:/wvdv coding/Python/11_WorkingWithJson/book.txt", "r") as f:
    data = f.read()
print(data)   

import json
book = json.loads(data)
print(book)
print(type(book))

print(book["Lipun"])
print (book["Lipun"]["email"])

for person in book:
    print(f"Name: {book[person]['name']}, Email: {book[person]['email']}, Phone: {book[person]['phone']}, Address: {book[person]['address']}")