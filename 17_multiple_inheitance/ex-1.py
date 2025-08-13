class Father():
    def gardening(self):
        print("i enjoy gardening")


class Mother():
    def cooking(self):
        print("i enjoy cooking")

# Father and Mother are base classes where Child is derieved classes

class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")


c = Child()
c.gardening()
c.cooking()
c.sports()

