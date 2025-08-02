# Pet Food Recommendation
# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food) .

species = str(input("enter species : " ))
age = int(input("enter age : "))


if species == "dog":
    if age < 2:
        print("Recommended food: Puppy food")
    elif age < 7:
        print("Recommended food: Adult dog food")
    else:
        print("Recommended food: Senior dog food")
elif species == "cat":
    if age < 2:
        print("Recommended food: Kitten food")
    elif age <= 5:
        print("Recommended food: Adult cat food")
    else:
        print("Recommended food: Senior cat food")
else:
    print("Sorry, recommendation is only available for Dog or Cat.")