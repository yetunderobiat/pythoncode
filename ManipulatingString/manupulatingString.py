# string literals

# double quotes
# spam = "this is robiat's cat"
# print(spam)

# #escape character
# spam = 'say hi to bob\'s mother.'
# spam = "say hi to bob\"s mother."
# print(spam)

# print("hello there! \n how are you? \n i\'m doing fine")

# #raw string
# print(r'That is carol\'s cats')

# # multiple string with triple quotes

# print(''' dear alice,'
#     this is robiat.
#     sincerly,
#     robiat
# ''')


# #multiline comments
# #indexing and slicing string

# print('How are you')
# feeling = input()
# if feeling.lower() == 'great' :
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')

# the isX string method
# isalpha() returns true if the string consists only of letters and is not blank
# print('hello'.isalpha()) 
# print('hello234'.isalpha())

# # isalnum() returns true if the string consists only of letters and numbers and is not blank
# print('hello234'.isalnum())
# print('hello'.isalnum())

# # isdecimal() returns true if the string consists only of numeric characters and is not blank
# print('234'.isdecimal())

# # isspace() returns true if the string consists only of spaces, tabs and new-lines and is not blank.
# print('   '.isspace())

# # istitle() returns true if the string consists only of words that begins with an uppercase letter followed by only lowercase letters
# print('This Is Title Case'.istitle())
# print('This Is Title Case 1233'.istitle())
# print('This is not Title case'.istitle())
# print('This is NOT Title case either'.istitle())



# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')

# while True:
#     print('Select a new password(letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers')



# the start with and end with method

# print('Hello world!'.startswith('Hello'))

# print('Hello world!'.endswith('world'))

# print('abc123'.startswith('abcdef'))

# print('abc123'.endswith('12'))

# print('Hello world!'.startswith('Hello world!'))

# print('Hello world!'.endswith('Hello world!'))

#the join and plit string method

# print(' ,'.join(['cats', 'rats', 'bats']))

# print('   '.join(['cats', 'rats', 'bats']))

# print('ABC'.join(['cats', 'rats', 'bats']))

# print('My name is robiat'.split('a'))

# # spam = ''' dear alice,'
# #     this is robiat.
# #     sincerly,
# #     robiat
# # '''
# # print(spam)
# # print(spam.split('\n'))

# # justifying text  with rjust(), ljust(), and center()
# # rjust()
# print('Hello'.rjust(10))
# print('Hello'.rjust(20))
# print('Hello world'.rjust(30))
# print('Hello'.rjust(10, '*'))
# # ljust()
# print('Hello'.ljust(20, '&'))
# # center()
# print('Hello'.center(20))
# print('Hello'.center(20, '='))

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# removing whitespac with strip(), rstrip(), and lstrip()

# spam = '    Hello World    '
# print(spam.strip())

# spam = '     Hello World'
# print(spam.rstrip())
# print(spam.lstrip())


# spam = 'Hello World'
# print(spam.lstrip())

# copying and pasting strings with the pyperclip module
import pyperclip
pyperclip.copy('Hello World')
pyperclip.paste()
print(pyperclip)


# adding bullet to wikimarkup