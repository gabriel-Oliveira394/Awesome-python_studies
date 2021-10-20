'''
Class variables and instance variables will often be utilized at the same time, so let’s look at an example of this
using the Shark class we created. The comments in the program outline each step of the process.
'''

class Shark:

    # Class Variable
    animal_type = 'fish'
    location = 'Ocean'

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        self.followers = followers
        print('This user has ' + str(self.followers) + ' followers.')


def main():
    # First object, set up instance variables of constructor method
    sammy = Shark('Sammy', 5)

    # print out instance variable name
    print(sammy.name)

    # print out class variable location
    print(sammy.location)

    # Second object
    stevie = Shark('Stevie', 8)

    # print out variable name
    print(stevie.name)

    # Use set_followers method and pass followers instance variable
    stevie.set_followers(77)

    print(stevie.followers)

    # Print out class variable animal_type
    print(stevie.animal_type)


if __name__ == '__main__':
    main()


'''
In object-oriented programming, variables at the class level are referred to as class variables, whereas variables at 
the object level are called instance variables.

This differentiation allows us to use class variables to initialize objects with a specific value assigned to variables,
 and use different variables for each object with instance variables.

Making use of class- and instance-specific variables can ensure that our code adheres to the DRY principle to reduce 
repetition within code.

'''