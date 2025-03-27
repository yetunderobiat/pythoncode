# 1. {}
# 2.
my_dict = {'foo':42}
# 3
#list ia an ordered collection of elements where each element are assigned by it's index while dictionaries is an unordered collection of keys and values pairs, where each is accessed using a key instead of an index 
# 4
# it will throw up a key error because the key 'foo' does not exist in the dictionary
# 5
# the difference is that 'cat' in spam is faster because it directly checks in the dictionary's internal storage while 'cat' in spam.keys() is slower because it creates an iterble view, adding overhead
# 6
spam = {'size':'large'}
spam.setdefault('color', 'black')
print(spam)
# 7
import pprint
information = {
    'firstName': 'robiat',
    'lastName' : 'ibrahim',
    'age': 10 
}
pprint.pprint(information)