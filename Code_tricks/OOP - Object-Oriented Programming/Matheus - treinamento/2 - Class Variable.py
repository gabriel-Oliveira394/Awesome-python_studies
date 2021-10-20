'''
Class variables are defined within the class construction. Because they are owned by the class itself, class variables
are shared by all instances of the class.

Defined outside of all the methods, class variables are, by convention, typically placed right below the class header
and before the constructor method and other methods.
'''



class Shark:
    animal_type = 'fish'
    location = 'ocean'
    followers = 5


new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

