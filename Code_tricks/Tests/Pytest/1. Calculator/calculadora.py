
class Calculadora:

    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def subt(n1, n2):
        return n1 - n2

    @staticmethod
    def times(n1, n2):
        return n1 * n2

    @staticmethod
    def division(n1, n2):
        try:
            return n1 / n2

        except ZeroDivisionError as error:
            print(error)


if __name__ == '__main__':
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    b = Calculadora()
    print(b.division(num1, num2))
    print(b.add(num1, num2))
    print(b.subt(num1, num2))
    print(b.times(num1, num2))

    user = 'Gabriel'
    print(f'{user=}')
