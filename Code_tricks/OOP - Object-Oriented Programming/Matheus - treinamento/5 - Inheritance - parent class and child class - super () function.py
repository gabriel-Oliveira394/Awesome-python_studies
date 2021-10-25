'''
Object-oriented programming creates reusable patterns of code to curtail redundancy in development projects.
One way that object-oriented programming achieves recyclable code is through inheritance, when one subclass can
leverage code from another base class.

'''

class Fish:
    def __init__(self, first_name, last_name='Fish',
                 skeleton='bone', eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_bachwards(self):
        print("The fish can swim backwards.")


class Trout(Fish):
    pass


class ClownFish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


casey = ClownFish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()

'''
The output shows that the Clownfish object casey is able to use the Fish methods __init__() and swim() as well as 
its child class method of live_with_anemone().

If we try to use the live_with_anemone() method in a Trout object, we’ll receive an error:
'''

terry.live_with_anemone()

