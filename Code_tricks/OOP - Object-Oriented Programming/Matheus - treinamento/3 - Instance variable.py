'''
Instance variables are owned by instances of the class. This means that for each object or instance of a class,
the instance variables are different.

Unlike class variables, instance variables are defined within methods.

'''


class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age


new_shark = Shark('Sammy', 5)
print(new_shark.name)
print(new_shark.age)

stevie = Shark('Stevie', 8)
print(stevie.name)
print(stevie.age)


'''
The stevie object, like the new_shark object passes the parameters specific for that instance of the Shark class to 
assign values to the instance variables.

Instance variables, owned by objects of the class, allow for each object or instance to have different values assigned 
to those variables.
'''

