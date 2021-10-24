class Calculator:

    @staticmethod
    def sum(n1, n2):
        return n1 + n2

    @staticmethod
    def subtraction(n1, n2):
        return n1 - n2

    @staticmethod
    def multiplication(n1, n2):
        return n1 * n2

    @staticmethod
    def division(n1, n2):
        if n2 == 0:
            raise ValueError("Divisão por zero não é permitido.")

        else:
            return n1 / n2




obj = Calculator()

choice = 1
while choice != 0:

    a = int(input("Enter first number:"))
    b = int(input('Enter the second number:'))

    print('1. ADDICTION')
    print('2. SUBTRACTION')
    print('3. MULTIPLICATION')
    print('4. DIVISION')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        print(obj.sum(a, b))
    elif choice == 2:
        print(obj.subtraction(a, b))
    elif choice == 3:
        print(obj.multiplication(a, b))
    elif choice == 4:
        print(obj.division(a, b))
    else:
        print('Invalid choice.')
