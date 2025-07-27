# Used to store Text data in Python

text = "Ice cream"  # store sequence of characters in different memory address
print(text)

# using index to access characters
text[0] # 'I'
text[1] # 'c' 

#text[2] ='t' # This line will raise an error because strings are immutable
# Strings are immutable, meaning they cannot be changed after creation

# sub indexing    
print(text[0:3])
print(text[4:9])
print(text[4:])  # This will print from index 4 to the end of the string
print(text[:3])  # This will print from the start of the string to index 3

print(text[-1])  # This will print the last character of the string
print(text[-2])  # This will print the second last character of the string

text = 'Ice  "cream" '
print(text)  # This will print the string with quotes included

address =  ''' 1 Odisha Street,
Bhubaneswar, Odisha,'''
print(address)  # This will print the multi-line string


s1 = "Hello"
s2 = "World"
S3 = s1 + " " + s2  # Concatenation of strings
print(S3)  # This will print "Hello World"

s = 'total states in India: '
number = 28
# total = s+number       # This will raise an error because you cannot concatenate a string and an integer directly
# To fix this, you can convert the integer to a string first    
total = s + str(number)  # Convert number to string before concatenation
print(total)  