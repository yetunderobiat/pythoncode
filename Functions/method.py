#methods
#method is the same thing as a function, except it is "called on" a value.

#finding a value in a list with the index() method
#list of values have an index method that can be passed by a value


# spam = ['hi', 'hello', 'hey']
# print(spam.index('hello'))

# spam = ['hi', 'hello', 'hey']
# spam.append('hola')
# print(spam)

# spam = ['hi', 'hello', 'hey']
# spam.insert(3, 'hola')
# print(spam)

# spam = ['hi', 'hello', 'hey']
# spam.remove('hi')
# print(spam)

# spam = ['hi', 'hello', 'hey']
# spam.sort()
# print(spam)

# spam = ['hi', 'hello', 'hey']
# spam.sort(reverse=True)
# print(spam)

# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key=str.lower)
# print(spam)

# import random

# message = ['it is certain',
#            'it is decidedly so',
#            'yes definitely',
#            'reply hazy try again',
#            'ask again later',
#            'my reply is no',
#            'outlook not so good',
#            'very doubtful']

# print(message[random.randint(0, len(message) -1)])

# list-like types: strings and tuples 
# name = 'Zophie'
# # print(name[0])
# # print(name[-2])
# # print(name[0:4])
# print('Zo' in name)
# print('z'  in name)
# print('p' not in name)

# mutable and immutable data type 
# A list value is a mutable data type: it can have values added, removed or changed
# A string is immutable it cannot be changed

# name = 'zophie a cat'
# name[7] = 'the'
# print(name)

# name = 'zophie a cat'
# newName = name[0:7] + 'the' + name[8:12]
# print(newName)

# eggs = [1, 2, 3]
# del eggs[2]
# del eggs[1]
# del eggs[0]
# eggs.append(4)
# eggs.append(5)
# eggs.append(6)
# print(eggs)

#the tuple data type
#the tuple data type is almost identical to the list data type except two ways.
#tuplesare typed with parenthenses,(and), instead of square brackets [and]

# eggs = ('hello', 42, 0.5)
# print(eggs[0])
# print(eggs[1:3])
# print(len[2])

# print(type(('hello',))) # this is a tuple
# print(type(('hello'))) #this is a list

#converting types with the list() and tuple() fnctions
# name = ('ayo', 'bayo', 'dayo')
# print(tuple(name))
# print(list(name))

#references
# a reference is a value that points to some bit of data 
#  a list reference is a value that
# spam = 42
# cheese = spam 
# spam = 100 # they are different variables that store different values

# print(spam)
# print(cheese)

# spam =  [0, 1, 2, 3, 4, 5]
# cheese = spam
# cheese[1] =  'Hello!'
# print(spam
# print(cheese)

#passing reference

# def eggs(someParameter):
#     someParameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

#the copy module's copy() and deepcopy fuctions

# import copy  

# spam = ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)
# cheese[1] = 42
# print(spam)
# print(cheese)

import copy  

spam = [['A', 'B', 'C', 'D'], ['a', 'b', 'c']]  
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam)
print(cheese)