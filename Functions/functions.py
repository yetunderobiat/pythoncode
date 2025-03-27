#a function is like a mini-program within a program.
#how to create your own function
# def hello(): #def means definition, hello is the name of a function
#     print("Howdy!")
#     print("Howdy!")
#     print("Hello there.")

# #A function cannot run unless the functionb is called or invoked
# hello()
# hello()
# hello()
# hello()

# #def statement with parameter
# def hello(name):
#     print('Hello' + name)

# hello('Alice')
# hello('Bob')

# #A parameter is a variable that passses value to it
# #def statement with adding two numbers
# def addnumber(a, b):
#     result = a + b
#     print(result)
# addnumber(3, 5)

# def addnum(a, b):
#     print(a + b)
# addnum(10, 30)


# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is deecidedly so'
#     elif answerNumber == 3:
#         return 'yes' 
#     elif answerNumber == 4:
#         return 'reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later' 
    
# rice = random.randint(1, 5)
# fortune = getAnswer(rice)
# print(fortune)

# print("cats", "dogs", "mice" )

#local and global scope
#  a variable that exists in a local scope is called a local variable.
#  global variable that exists in a global scope is called a global variable.
# local variables can not be used in a global scope

# def name():
#     firstName = "Robiat"
#     print(firstName)
# name()

# def details():
#     lastName = "Ibrahim"
#     print(firstName + lastName)
# details()

# def spam():
#     eggs = 99
#     print(eggs)
    

# def bacon():
#     ham = 101
#     eggss = 0
#     print(eggss)

# spam()
# bacon()


# def spam(dividedBy):
#     return 42 / dividedBy
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

def spam(dividedBy):
    try:
    except ZeroDivisionError:
        return 42 / dividedBy
        print('Error: number must be greater than 0')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))