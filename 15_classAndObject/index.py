# class in Python is a blueprint for creating objects
# an object is an instance of a class
# let human is a class - Name,gender,occupation are properties of the class and  speaks,do works,sleep are methods of the class


class Human:
    def __init__(self,n,o):
        #properties
        self.name = n
        self.occupation = o

# methods
    def do_work(self):
        if self.occupation == "doctor":
            print(self.name,"is a doctor") 
        elif self.occupation == "engineer":
            print(self.name,"is an engineer")
    
    def speaks(self):
        print(self.name,"says hello")


  # instance of the class
Lipun = Human("Lipun","doctor")
Lipun.do_work()
Lipun.speaks()    


Papun = Human("Papun","engineer")
Papun.do_work()
Papun.speaks()