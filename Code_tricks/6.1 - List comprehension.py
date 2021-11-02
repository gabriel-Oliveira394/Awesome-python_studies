'''
I have a store and to control the itens that I sell, I have a list with the prices of my products.
'''

dic_precos = {'camisa':500,
              'calça': 250,
              'sapato':325,
              'cinto': 50,
              'meia': 23.99}

print(type(dic_precos))
print(dic_precos)

nova_lista_precos = []

for preco in dic_precos:
    nova_lista_precos.append(preco * 2)

print(nova_lista_precos)


print([dic_precos[i]*2 if dic_precos[i] > 100 else 0 for i in dic_precos])

for i in dic_precos:
    print(i)
    print(dic_precos[i])