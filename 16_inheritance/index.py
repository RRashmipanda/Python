# inheritance is a way to form new classes using classes that have already been defined.
# example car and bikes are classes that inherit from the vehicle class

class Vehicle:
    def general_usage(self):
        print("general use: transportation")

# Vehicle is the base class, Car and Bike are derived classes
# derived classes inherit attributes and methods from the base class

class Car(Vehicle): # Car inherits from Vehicle, Vehicle -base class, Car - derived class
    def __init__(self):
        print("i am car")
        self.wheels = 4
        self.has_roof = True
 
    def specific_usage(self):
        self.general_usage()  # calling method from base class
        print("specific use: transporting people and goods")

class Bike(Vehicle): # Bike inherits from Vehicle
    def __init__(self):
        print("i am bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific use: transporting people")


# you can call methods from the base class using the derived class objects
# car and bikes are derived classes of vehicle and c ,b are objects of those classes

c = Car()
c.general_usage() # calling method from base class
c.specific_usage()

b= Bike()
b.general_usage() # calling method from base class  
b.specific_usage()



# Benefits of inheritance:
# 1. Code Reusability: You can use existing code without rewriting it.
# 2. Method Overriding: You can change the behavior of a method in the derived class.
# 3. Extensibility: You can add new features to derived classes without modifying the base class. like in car has specific_usage method
# 4. Readability: It makes the code more organized and easier to understand.


# isinstance and issubclass are used to check the type of an object or class 
c = Car()
b = Bike()
print(isinstance(c, Car))
print(issubclass(Car, Vehicle)) 
print(issubclass(Bike,Car)) # False, Bike is not a subclass of Car



