'''
I have a store and to control the itens that I sell, I have a list with the prices of my products.
'''

lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)

print(nova_lista_precos)

# ---- List Comprehension ----
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)


'''
Todos os produtos que custam mais de 1000 dolares eu vou pagar um imposto de 50% sobre o valor total.
'''

imposto = []

for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco * 0.5)

    else:
        imposto.append(0)

print(f'O imposto pago por produto: {imposto}')
print(f'O total pago é: {sum(imposto)}')

# --- list comprehension ---

imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
imposto3 = [preco * 0.5 if preco > 1000 else 0 for preco in lista_precos]

print(imposto2)
print(imposto3)


# --------

squares = []
for i in range (1, 101):
    squares.append(i**2)

print(squares)

squares = [i ** 2 for i in range(1, 101)]

squares2 = [x**2 % 5 for x in range(1,101)]


listinha = [2, -3, 1]
print(4*listinha)
print([i*4 for i in listinha])


# Cartesian product

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)


# complex cartesian product

A = [1, 2, 3, 4, 5]
B = ['a', 'b', 'c', 'd', 'e']
C = ['I', 'II', 'III', 'IV', 'V']

cartesian_product2 = [(a,b,c) for a in A for b in B for c in C]
print(cartesian_product2)
print(len(cartesian_product2))

# list comprehension https://www.youtube.com/watch?v=EL--NjvBw6o

list1 = [1,2,3]

print([i for i in list1])
print([i * 5 if i == 3 else i for i in list1])

# se eu quero só um IF, ele deve estar do lado direito

# print([i*5 if i == 3 for i in list1 ])
print([i*5 for i in list1 if i == 3])

# se eu quero colocar um IF e um ELSE, ambos devem estar do lado esquerdo
print([i*5 if i == 3 else i for i in list1])

