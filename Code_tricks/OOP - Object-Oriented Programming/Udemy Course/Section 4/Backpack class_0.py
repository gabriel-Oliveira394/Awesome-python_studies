class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color


my_backpack = Backpack("blue")
your_backpack = Backpack("red")
print(my_backpack.color)
print(your_backpack.color)

print("Changing colors...")
my_backpack.color = "green"
print(my_backpack.color)
print(your_backpack.color)