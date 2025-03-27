# finding pattern of text without regualr expression
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# print( '080-333-5555 is a phone number')
# print(isPhoneNumber('080-333-5555'))
# print('moshi moshiis a phone number:')
# print(isPhoneNumber('moshi moshi'))

# creating regex objects
# A regex object's search() method searches the string it is passed for any matches to the regex. 
# The search() method will return Noneif the regex pattern is not found in the string. if the pattern is found, the search() method returns a match object.
# Match objects have a group() method that will return the actual matched text from the searched string.
# import re
# phoneNumRegek = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegek.search('My name is 415-555-4242. ')
# print('Phone number found: ' + mo.group())

# review  of  regular expression matching
# 1. import the regex module with import re.
# 2. create 


#grouping with parenthesis
# import re
# phoneNumRegek = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegek.search('My name is 415-555-4242. ')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)


# import re
# phoneNumRegek = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegek.search('My name is (415) 555-4242. ')
# print(mo.group(1))
# print(mo.group(2))


# Matching multiple groups with the pipe (| -- this is called pipe)
# import re
# heroRegex = re.compile (r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and tina fey')
# print(mo1.group())

# heroRegex = re.compile (r'Tina Fey|Batman')
# mo1 = heroRegex.search('Tina Fey and Batman')
# print(mo1.group())

# batRegex = re.compile (r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))


#  optional matching with the question mark
# batRegex = re.compile (r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventure of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventure of Batwoman')
# print(mo2.group())

# phoneNumRegek = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneNumRegek.search('My name is -415-555-4242. ')
# print(mo1.group())


# mo2 = phoneNumRegek.search('My name is 555-4242. ')
# print(mo2.group())

# batRegex = re.compile (r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventure of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventure of Batwowowowowoman')
# print(mo2.group())

# matching specific repetitions with curly brackets
# import re
# haRegex = re.compile(r'(ha){3}')
# mo1 = haRegex.search('hahaha')
# print(mo1.group())

# mo2 = haRegex.search('ha')
# print(mo2 == None)

# greedy and nongreedy matching
# greedyHaRegex = re.compile(r'(ha){3,5}')
# mo1 = greedyHaRegex.search('hahahahaha')
# print(mo1.group())

# nongreedyHaRegex = re.compile(r'(ha){3,5}?')
# mo2 = nongreedyHaRegex.search('hahahahaha')
# print(mo2.group())

#The findall() method
# import re
# phoneNumRegex =  re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # the regular expression
# mo = phoneNumRegex.search('Work: 212-555-0000 cell: 415-555-9999 ')
# print(mo.group())

# mo1 = phoneNumRegex.search(' cell: 415-555-9999 Work: 212-555-0000')
# print(mo1.group())



# print(phoneNumRegex.findall(' cell: 415-555-9999 Work: 212-555-0000'))

# making your own character class
# import re
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats abby food. BABY FOOD.'))

# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats abby food. BABY FOOD.'))

# the caret and dollar sign character(^,$)
# import re
# beginsWithHello = re.compile(r'^Hello')
# beginsWithHello.search('Hello world')
# print(beginsWithHello.search('He said hello.') == None)

# endsWithNumber = re.compile(r'\d$')
# endsWithNumber.search('Your number is 42')
# print(endsWithNumber.search('Your number is forty two') == None)

# The wild card character
# import re
# atRegex = re.compile(r'.he')
# print(atRegex.findall('The cat in the hat sat on the flat mat'))

# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat'))

# matching everything with dot star(.*)
# import re
# nameRegex = re.compile(r'First Name:  (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Robiat Last Name: Ibrahim') 
# print(mo.group(1))
# print(mo.group(2))

# matching newlines  with the dot character
# import re
# noNewlineRegex = re.compile('.*')
# print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# newlineRegex = re.compile('.*', re.DOTALL)
# print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# case-insensitive matching
# import re
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('RoboCop is part man, part machine, all cop.').group())

#substituting strings with the sub() method
import re
# namesRegex = re.compile(r'Agent')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# managing complex regexes
# import re
