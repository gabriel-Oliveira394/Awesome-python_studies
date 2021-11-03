class Donut:
    def __init__(self, flavor, toppings, filling, size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size


donut1 = Donut("sugar", "caramel", "chocolate", "big")
print(donut1.flavor)
print(donut1.toppings)
print(donut1.filling)
print(donut1.size)
