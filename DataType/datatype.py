#This is my first program 5/02/2025
# print("hello world")

# #string
# name="robiat"   
# print(name)


# #integer
# num=10          
# num2=3.5
# print(num)
# print(num2)


# #boolean either true/false
# isFemale = True  
# print(isFemale)


# a=6
# b=2

# if(a<b):
#   print("A is the biggest")
# else:
#   print("B is the biggest")


# result=(a+b)
# result=(a-b)
# result=(a%b)
# print(result)


# #string
# firstName="Robiat"
# secondName="Ibrahim"
# fullname=firstName + secondName
# print(fullname)


# #escape character
# favorite="My name is robiat.n i love to eat"
# print(favorite)


# #string repetition
# name="robiat"
# print(name*4)


#string typecasting
# name="robiat"
# print(name+ str(4))


# #string array
# name="Robiat"
# print(name[4])


# #in operator
# name="robiat"
# print("i" in name)


#built-in string
# name="robiat"
# print(name.__len__())

# name= "robiat"
# print(name.upper())#


# name = "       Robiat"
# print(name.lstrip())


# #string.isalnum
# name = "     robiat"
# print(max(name.lstrip()))

# name = "Robiat"
# print(min(name)
#

# items = ["tomatoes", "oranges", "pineapples", "guevas", "mangoes"] #every list can be accessed by its index number
# print(items[2])



# items = ["tomatoes", "oranges", "pineapples", "guevas", "mangoes"] #every list can be accessed by its index number
# num = [0, 3, 4, 6, 7, 6, 3, 2]
# print(max(num))

# items.append(num)
# print(items)

# items.insert(3, "onion")
# print(items)

# items.insert(3, "onion")
# items.pop()
# print(items)

# items.remove("guevas")
# print(items)

# items.sort()
# print(items)

# items.reverse()
# print(items)

# items.index(mangoes)
# print(items)

# items.extend(num)
# print(items)

#slicing list
# items = ["tomatoes", "oranges", "pineapples", "guevas", "mangoes"] #every list can be accessed by its index number
# num = [0, 3, 4, 6, 7, 6, 3, 2]

# result = num[4:-2]
# print(result)

# result = num[3:6]
# print(result)

# result = num[:3]
# print(result)

# result = num[2:]
# print(result)

# result = num[::5]
# print(result)

# result = num[4::]
# print(result)





#TUPLES
# It is a series of immutable(doesn't change) objects. It is a sequence identical to a list. It is similar to list. 
#It uses () unlike list

# myTuple = (1,2,3,4,5,6)
# myList = [1,2,3,4,5]
# print(myTuple)
# print(myList)
# print(type(myTuple)) #it shows what data type it is
# print(type(myList))


#DICTIONARIES
#it is a data structure that has an efficient value/key hash table termed as 'dict'. It uses {} brackets

# dict1 = {}
# dict1['rd'] = "red"
# dict1['yel'] = "yellow"
# dict1['bl'] = "blue"
# print(dict1)

dict1 =  {'nm':'festus', 'age':30, 'height':5.7} #this is an object of a dictioanry
# 'nm', 'age', 'height' are keys
# 'festus', '30', '5.7'  are values
# print(dict1.keys()) #it will print the list of keys
# print(dict1.value()) #it will print the list of value

# print(len(dict1)) #checking the length
# print(str(dict1)) # it repeats the object
# print(type(dict1)) #it specifies what data type it is


#CLEAR 
# dict1.clear()
# print(dict1)

#COPY
# dict2 = dict1.copy()
# print(dict2)

#GET
# dict1.get('nm')
# print(dict1)

#HAS
# dict1.has()
# print(dict1)

#ITEMS 
# print(dict1.items())

# #KEYS
# print(dict1.keys())

# #VALUES
# print(dict1.value())

#UPDATES
anotherdic = {'complextion' : 'black'}
dict1.update(anotherdic)
print(dict1)


#python programs are composed of modules, statement, expressions, and objects
#they involve implementing built-in or user-defined 