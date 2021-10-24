def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero.')

    else:
        return n1 / n2


def divide2(m1, m2):
    try:
        return m1 / m2

    except ZeroDivisionError as error:
        print(error)


def divide3(k1, k2):
    try:
        return k1 / k2
    except:
        raise ValueError('não se pode dividir por zero')


print(f'Resultado: {divide3(1, 0)}')
