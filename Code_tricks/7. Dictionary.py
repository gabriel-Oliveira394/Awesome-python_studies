
'''
I am using this tutorial: https://www.datacamp.com/community/tutorials/dictionary-python?utm_source=adwords_ppc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-763347114660:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001566&gclid=Cj0KCQjww4OMBhCUARIsAILndv7NS08uIN5oseQvcNULL9690xQPgXcy9uY-8k6RY7yIikPLT88BUMEaAgeEEALw_wcB
'''


dic_precos = {'camisa':500,
              'calça': 250,
              'sapato':325,
              'cinto': 50,
              'meia': 23.99}

print(type(dic_precos))
print(dic_precos)

'''
If you define a dictionary key with a mutable results in a TypeError. Dictionaries keys must be immutable types.
Instead, you can use a tuple
'''


dic_precos = {'camisa':500,
              'calça': 250,
              'sapato':325,
              'cinto': 50,
              'meia': 23.99,
              #['meia', 'cinto', 'camisa'] : 523,
              ('meia', 'cinto', 'camisa') : 523}

print(dic_precos)


'''
accessing keys and values: 

1. To access the key value pair, you would use the .items() method;
2. To access the keys separately, you could use the .keys() method;
3. To access the values separately, you could use the .values() method.
'''

print(dic_precos.items())
print(dic_precos.keys())
print(dic_precos.values())

for key, value in dic_precos.items():
    print(key, end=',')

for key, value in dic_precos.items():
    print(value, end=',')


'''
You can access a value by specifying a key as a parameter
'''

print('\n O preço da camisa é: ', dic_precos['camisa'])


'''
Nested Dictionary: a dictionary is passed as a value to a key of the main dictionary.

'''

dictionary_nested = {"datacamp":{"Deep Learning": "Python", "Machine Learning": "Pandas"},"linkedin":"jobs",
                     "nvidia":"hardware"}

print(dictionary_nested)
print(dictionary_nested['datacamp'])
print(dictionary_nested['datacamp']['Deep Learning'])


'''
Dictionary Comprehension

It can be used to create dictionaries from arbitrary key and value expressions. 
It is a simple and concise way of creating dictionaries and is often faster than the usual for loop implementations.

'''

import time

t1 = time.time()
dict_comprehension = {i: i**3 for i in range(200000)}
print(time.time() - t1)
print(len(dict_comprehension))

# print the first 10 keyL value pairs from the dict_comprehension dictionary.

from itertools import islice

comp_10 = list(islice(dict_comprehension.items(), 10))
print(comp_10)

# ---------------------------------------------

t1 = time.time()
dict_comprehension = dict()
for i in range(200_000):
    dict_comprehension[i+1] = i**3

print(time.time() - t1)

# As you can see, the list comprehension decrease the time it takes to implement the dictionary.
# ---------------------------------------------

'''
Word Frequency: 
'''

corpus = 'learn all about the Python Dictionary and its potential. \
            You would also learn to create word frequency using the Dictionary'

word_freq = dict()
corpus_word = str(corpus).split()

for i in range(len(corpus_word)):
    if corpus_word[i] not in word_freq:
        word_freq[corpus_word[i]] = 1

    else:
        word_freq[corpus_word[i]] += 1

    print(word_freq)

# ------------------------------------------

message = 'O senhor é o meu pastor e nada me faltará. Esse é um salmos bastante famoso e em muitas residências é possível' \
          ' ver q as pessoas o colocam nas paredes e mesas. Mas aqui eu deixo uma pergunta: será que elas sabem de fato' \
          ' o que esse salmos significa? O que será que significa o Senhor ser o nosso pastor? O Senhor ser o nosso pastor' \
          ' é algo que nos trás paz e confiança no futuro. Pq temos a certeza que dias melhores virão, basta termos fé.'

message_word = str(message).split()

print(message_word)

dict_message_word = dict()

for i in range(len(message_word)):
    if message_word[i] not in dict_message_word:
        dict_message_word[message_word[i]] = 1
        
    else:
        dict_message_word[message_word[i]] += 1
        
print(dict_message_word)