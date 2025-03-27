# #write a function that calculates the area of a circle a =pier^

# def areaofacircle(p, r):
#     result = p * r * r
#     print(result)

# areaofacircle (3.142, 5)

# # write a function that converts fahrenheits to celcius c= 5/9 x (f-32)

# def converttocelcius(f):
#     result = 5/9 * (f - 32)
#     print(result)

# converttocelcius(5)

# # write a function that converts from celcius to farenheit f=(9/5 * c)+32
# def converttofahrenheits(c):
#     result = (9/5 * c) + 32
#     print(result)

# converttocelcius(-45)


import random

secretNumber = random.randint(1, 20)
print('Im thinking of a number btee 1 and 20')

for guessTaken in range(1, 7):
    print ('take a guess: ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print('good job!yo guessed my number in ' + str(guessTaken) + 'guesses!')
else:
    print('nope, the number i was thinking of was ' + str(secretNumber))