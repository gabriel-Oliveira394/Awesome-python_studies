'''
We are creating an item attribute for an instance (self) being created and initially it is empty.
'''


class Backpack:

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []


my_backpack = Backpack('blue', 70)
print(my_backpack)