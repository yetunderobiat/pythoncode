import random

secretNumber = random.randint(1, 20)
print("Im thining of a random number from 1 to 20")

for guessTaken in range(1, 7):
    print("Im taking a guess")
    guess = int(input())

    if guess < secretNumber:
        print("vhjjhbbji")
    elif guess > secretNumber:
        print("yccvyuy")
    else:
        break


if guess == secretNumber:
    print("guess taken correctly" + str(guessTaken)  + "guess")
else:
    print("try again" + str(secretNumber))

    