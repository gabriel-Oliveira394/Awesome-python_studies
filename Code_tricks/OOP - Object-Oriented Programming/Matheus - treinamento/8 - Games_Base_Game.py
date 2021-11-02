import abc
import random
import matplotlib.pyplot as plt
from random import randint


class BaseGame(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        """Main method to run the game."""
        pass

    @abc.abstractmethod
    def _input_check(self):
        """Check user input."""
        pass


class DiceRolling(BaseGame):
    """Rolling a dice."""

    def number():
        return randint(1, 6)

    repeat = True
    while repeat:
        numb = input("Roll dice? (y/n):")

        if numb == 'y':
            print(number())

        elif numb == 'n':
            print("0")
            repeat = False

        else:
            print("You must type 'y' or 'n'! Try again...")
