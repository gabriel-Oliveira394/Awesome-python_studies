class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone)
    pass


great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()

'''
The output shows that methods from both parent classes were effectively used in the child class.

Multiple inheritance allows us to use the code from more than one parent class in a child class. If the same method is 
defined in multiple parent methods, the child class will use the method of the first parent declared in its tuple list.

Though it can be used effectively, multiple inheritance should be done with care so that our programs do not become 
ambiguous and difficult for other programmers to understand.

# Conclusion
This tutorial went through constructing parent classes and child classes, overriding parent methods and attributes 
within child classes, using the ```super()``` function, and allowing for child classes to inherit from multiple parent 
classes.

Inheritance in object-oriented coding can allow for adherence to the DRY (don’t repeat yourself) principle of software 
development, allowing for more to be done with less code and repetition. Inheritance also compels programmers to think 
about how they are designing the programs they are creating to ensure that code is effective and clear. 
'''
