class Father():
    def skills(self):
        print("coding, gardening")


class Mother():
    def skills(self):
        print("art, cooking")

# Father and Mother are base classes where Child is derieved classes

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sports")


c = Child()
c.skills()

