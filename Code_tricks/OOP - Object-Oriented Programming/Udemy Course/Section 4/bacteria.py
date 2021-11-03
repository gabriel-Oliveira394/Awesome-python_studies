class Bacterium:

    def __init__(self, size, amount, x, y):

        self.size = size
        self.amount = amount
        self.x = x
        self.y = y


bac1 = Bacterium(7, 100, 1.2, 3.4)

print(bac1.size)
print(bac1.amount)
print(bac1.x)
print(bac1.y)

