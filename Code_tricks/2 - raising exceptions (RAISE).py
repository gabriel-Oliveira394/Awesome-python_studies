'''
I can raise an Exception very quickly with python
>>> import builtins
>>> help(builtins)

'''


class CoffeeCup:
    def __init__(self, temperature):
        self.temperature = temperature

    def drink_coffee(self):
        if self.temperature > 85:
            raise Exception('Coffee is too hot!')

        if self.temperature < 65:
            raise ValueError('Coffee is too cold!')

        else:
            print('Coffee is okay to drink.')


cup = CoffeeCup(175)
cup.drink_coffee()

