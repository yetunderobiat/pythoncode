# the dictionary data type

# dictionaries use {} brackets
#dictionaries are unordered list unlike list 

# myCat = {'size': 'fat', 'color':'gray', 'disposition': 'loud'}
# print(myCat['size'])

# myNames = {'firstname':'robiat', 'secondname':'yetunde', 'thirdname':'ibrahim'}
# print(myNames['secondname'])
# print('my first name is '+''+ myNames['firstname']+''+ ' and my second name is '+''+myNames['secondname']+''+ ' and my third name is '+''+myNames['thirdname'])

# print('my cat has' + '' + myCat['color'] + '' + 'fur')

# birthdays = {'Alice': 'apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter your name: (blank to quit)')
#     name = input()
#     if name == '':  
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')



# birthdays = {'Alice': 'apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# for v in birthdays.values():
#     print(v)

# for k in birthdays.keys():
#     print(k)

# for i in birthdays.items():
#     print(i)

# spam = {'Alice': 'apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# print(list(spam.keys()))
# print(tuple(spam.keys()))

# spam = {'Alice': 'apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# for  k, v in spam.items():
#     print('Key: ' + k + ' value: ' + str(v))


# checking whether a key or value exist in a dictionary
# spam = {'Alice': 'apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# print('name' in spam.keys())
# print('apr 1' in spam.values())
# print('Carol' in spam.keys())

# picnicItems = {'apples': 5, 'cups':2}
# print('I a bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

# print('I a bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# the setdefault() method
# spam = {'name': 'pooka', 'age':5}
# print(spam.setdefault('color', 'black'))

# spam 
# {'name': 'pooka', 'age':5, 'color':'black'}
# print(spam.setdefault('color', 'black'))

# message = 'It was a bright cold day in april, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# print(count)

# pretty printing
# import pprint

# message = 'It was a bright cold day in april, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# pprint.pprint(count)

# import pprint

# message = 'It was a bright cold day in april, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# # pprint.pprint(count)
# print(pprint.pformat(count))

#Nesterd dictiaries and lists
allGuests = {
            'Alice': {'apples': 5, 'pretzel': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies':1}
            }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of thing being brought:')
print(' - Apples               '+ str(totalBrought(allGuests,'apples')))
print(' - cups                 '+ str(totalBrought(allGuests,'cups')))
print(' - Cakes                '+ str(totalBrought(allGuests,'Cakes')))
print(' - Ham sandwiches       '+ str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies           '+ str(totalBrought(allGuests, 'apple pies')))


# fantasy game inventory
# you are creating a fantasy video game. the data structure to model the player's inventory will be a dictionary where the keys are string values 
# describing the item in the inventory and the value is an integer value detailing how much of that ite the player has. for example, the dictionary value
# {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
# write a 


# inventory.py
stuff = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12} 

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)