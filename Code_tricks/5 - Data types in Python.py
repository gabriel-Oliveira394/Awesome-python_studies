# String
d = 'Gabriel'
print(d, type(d))

# integers
d = 10
print(d, type(d))

# floats
d = 3.141516
print(d, type(d))

# boolean
d = True
print(d, type(d))

# lists
d = ['Gabriel', 10, 3.1415, True]
print(d, type(d))

# Tuples
d = ('Gabriel', 10, 3.141516, True)
print(d, type(d))

# Dictionaries
d = {'Gabriel':10,
     'Joaine':20,
     'Priscila':30,
     'Larissa':40,
     'Lizziane':50}
print(d, type(d))

# sets
d = {1, 2, 3}
print(d, type(d))

# Python program to demonstrate the Creation of Set in Python

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with a mixed type of values (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)