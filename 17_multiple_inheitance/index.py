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