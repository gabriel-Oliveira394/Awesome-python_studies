"""

What Is Polymorphism?
Polymorphism is an important feature of class definition in Python that is utilized when you have commonly named
methods across classes or subclasses. This allows functions to use objects of any of these polymorphic classes
without needing to be aware of distinctions across the classes.

Polymorphism can be carried out through inheritance, with subclasses making use of base class methods or overriding
them.

"""


class Shark():
    def swim(self):
        print("The Shark is swimming.")

    def swim_backwards(self):
        print("The Shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


sammy = Shark()
# sammy.skeleton()

casey = Clownfish()
# casey.skeleton()


for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()


# --------------------------------------

def in_the_pacific(fish1):
    fish1.swim()


in_the_pacific(sammy)
in_the_pacific(casey)
