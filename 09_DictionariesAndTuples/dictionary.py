# Dictionary allows you to store key-value pairs, also known as associative arrays or hash maps.

d = {"tom" :9933939293, "jerry": 9933939292, "spike": 9933939291}
print(d)
# Accessing values using keys
print(d["tom"])
d["LIPUN"] = 9329941045
print(d)
# order does not matter in dictionaries

# Deleting a key-value pair
del d["jerry"]
print(d)

# Checking if a key exists
if "tom" in d:
    print("Tom's number is:", d["tom"])

#print key with value
for key in d:
    print("key:",key,", value:",d[key])   
for k,v in d.items():
    print("key:", k, "value:", v)
d.clear()  # This will remove all items from the dictionary
print("After clearing:", d)    