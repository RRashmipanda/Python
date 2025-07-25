a = 12+34
print(a)

b = 56-78
print(b)

c = 90*12
print(c)

d = 144/12
print(d)

e = 5**3
print(e)

f = 100 % 6
print(f)

# problem - Like you want to travel 124 km and you have a vehicle that can travel 60 km in one hour. How many hours will it take to travel 124 km?
distance = 124
speed = 60
time = distance / speed
print(time)

# If you want to find time in 2 decimal points
time = round(time, 2)
print(time)


ABB = 10 + 2*3
print(ABB)

ABBB = (10+2)*3
print("ABBB =", ABBB)

ABC = 10 + 2*3 - 5
print(ABC)

ABD = 10 + 2*3 - 5 + 8
print(ABD)

ABE = 10 + 2*3 - 5 + 8 / 2
print(ABE)

# If you want to Print the value of ABE without any decimal points
ABE = round(ABE)
print(ABE)

# when floating numbers are store they always loose accuracy
# No precise way to store floating numbers
Z = 6-5.7
print(Z)
roundZ = round(Z, 2)
print(roundZ)
