"""

Object-oriented programming (OOP) focuses on creating reusable patterns of code, in contrast to procedural programming, 
which focuses on explicit sequenced instructions. When working on complex programs in particular, object-oriented 
programming lets you reuse code and write code that is more readable, which in turn makes it more maintainable.

- Class — A blueprint created by a programmer for an object. This defines a set of attributes that will characterize
any object that is instantiated from this class.

- Object — An instance of a class. This is the realized version of the class, where the class is manifested in the
program.

These are used to create patterns (in the case of classes) and then make use of the patterns (in the case of objects).

the def we have inside a class is a METHOD - a special kind of function that are defined within a class.

Classes are useful because they allow us to create many similar objects based on the same blueprint.
"""


class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is the constructor method.")

    def swim(self):
        print(self.name + ' is swimming.')

    def be_awesome(self):
        print(self.name + " is being awesome.")

    def age_shark(self):
        print(self.age, "years old.")

# we already have a blueprint to create the object shark.


def main():
    sammy = Shark('Sammy', 5)
    sammy.swim()
    sammy.be_awesome()
    sammy.age_shark()

    stevie = Shark('stevie', 7)
    stevie.swim()


if __name__ == "__main__":
    main()
