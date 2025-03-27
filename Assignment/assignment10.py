def isPhoneNumber(text):
    if len(text) != 11:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print( 'my phone number is: 080-3335-1395 ')
print(isPhoneNumber('080-3335-1395'))

import re
phoneNumRegek = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegek.search('My number is 080-3335-1395.')
print('My phone number is:')
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)