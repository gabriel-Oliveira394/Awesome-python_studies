# sorting
temp_list = [12, 6, 9]

# normal sorting
sorting = sorted(temp_list)
print(f'Normal sorting: {sorting}')

# reverse option
sorting = sorted(temp_list, reverse=True)
print(f'reverse option: {sorting}')

# unordered tuple_list

'''
I want to order a list of tuple based on the second argument of the tuple
'''
tuple_list = [('a', '2'), ('c', '1'), ('d', '3'), ('a', '3')]
func = lambda x: x[1]
sorting = sorted(tuple_list, key=func)
print(f'Order the list {tuple_list}, based on the second argument: \n {sorting}')

'''
I have a capitalized letter A and also a lower case letter 'a'. If we sort it will prioritize the capital letters. 
'''

tuple_list = [('A', '2'), ('a', '1'), ('D', '3'), ('b', '3')]
sorting = sorted(tuple_list)
print(f'\n it will prioritize the capital letters: \n {sorting}')

'''
Imagine we want to ignore the capitalized case. We can use the function casefold as shown below.
'''

func = lambda x: str.casefold(x[0])
sorting = sorted(tuple_list, key=func)
print(f'\n Ignoring the capital letters prioritization: \n {sorting}')


'''
Imagine if we have the same letter, the sorting being based on the second element.
'''

tuple_list = [('a', '4'), ('c', '1'), ('d', '3'), ('a', '3')]
sorting = sorted(tuple_list, key = lambda x: x[0])
print('\n', sorting)

# let's solve this problem:

func = lambda x: (x[0], x[1])
sorting = sorted(tuple_list, key=func)
print('\n vuoooola: ', sorting)


# Top d+! Glórias a Deus :)


