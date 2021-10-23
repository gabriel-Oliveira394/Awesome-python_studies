
class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return int(self.num1) + int(self.num2)

    def subt(self):
        return int(self.num1) - int(self.num2)

    def times(self):
        return int(self.num1) * int(self.num2)

    def division(self):
        if self.num2 == 0:
            print(f'Error, division by zero. Try again!')

        else:
            return int(self.num1) / int(self.num2)


if __name__ == '__main__':
    num1 = input('First number: ')
    num2 = input('Second number: ')
    b = Calculadora(num1, num2)
    print(b.add())
    print(b.subt())
    print(b.times())
    print(b.division())

    user = 'Gabriel'
    print(f'{user=}')
