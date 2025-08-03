# Reverse a String
# Reverse a string using a loop.

input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)

# On each loop iteration, char + reversed_str adds the new character at the front of the existing string.

