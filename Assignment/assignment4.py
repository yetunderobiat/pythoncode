#imports in python
# loop through digits from 1 to 10 create a variable and pass the values
# loop through one to ten then break the loop at five and printthe result
# n = 1,2,5 if the modulus of this number is = 0 multiple n by 2 and continue if it is else just print the number
# read branching in python


# # 1
# numbers = [] #create an empty list to store the values

# for i in range(1, 11): #range function generates a sequence of number starting from a specified start value, stopping before a specified stop valueand stepping by a specified step value. 
#     starting_num = i #i created a variable and assign the current value
#     numbers.append(starting_num)

# print(numbers)


# # 2
# numbers = [] #create an empty list to store the values

# for i in  range(1, 11): # i is called the loop variable or iterator variable
#     numbers.append(i)

#     if i == 5:
#         break

# print("Results:", numbers)


# # 3
# numbers = [1, 2, 3]

# for n in numbers:
#     if n % 2 == 0:
#         n *= 2
#     print(n)


#Branching in python
# Branching refers to the control structure that allows a program to execute different blocks of code based on conditions and decisions
# In python, branching is achieved using the if statements, if-else statement, and elif statement

# #If statement - it is used to execute a block of code if the condition is true

# a = 50
# b = 30

# if a > b:
#     print("Correct, A is bigger")


# # If-else statement - it executes one block of code if a condition is true and another block of  code if the condition is false
# x = 90
# y = 100
# z = 120

# if x < y > z:
#     print("Correct")
# else:
#     print("Incorrect")

# Elif statement - they are used to check multiple conditions and execute different blocks of codes based on those conditions

# a = 2
# b = 4
# c = 6
# d = 2

# if a > c:
#     print("Correct")
# elif b < c:
#     print("correct")
# elif a == c:
#     print("The same")
# else:
#     print("Wrong input")
