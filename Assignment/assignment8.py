# 1. What are the two values of the Boolean data type? How do you write  them? 
# True
# False

# 2. What are the three Boolean operators?
# AND && – Returns True if both conditions are True, otherwise False. 
# OR  – Returns True if at least one condition is True.
# NOT ! – Reverses the Boolean value.

# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

# AND && Operator
# Returns True only if both values are True.

# A	    B	    A AND B 
# True	True	True
# True	False	False
# False	True	False
# False	False	False

# OR Operator
# Returns True if at least one value is True.

# A	    B	    A OR B 
# True	True	True
# True	False	True
# False	True	True
# False   False   False

# NOT ! Operator
# Reverses the Boolean value.

# A	    NOT A 
# True	False
# False	True

# 4. a. false
# b. false
# c. true
# d. false
# e. false
# f. true

#  5. What are the six comparison operators?
# Greater than (>)
# Less than (<)
# Less than or equal to (<=)
# Equal to (==)
# Not equal to (!=)

# 6. What is the difference between the equal to operator and the assignment operator?
# Comparison Operator is used to check if two values are equal whike the Assignment Operator is used to assign a value to a variable.

# 7. Explain what a condition is and where you would use one.
# A condition is an expression that evaluates to either True or False.
# if Statements
# if-else 
# Loops (while, for)

# 8. Identify the three blocks in this code:

spam = 0

if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
print('spam')

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input("Enter a number: ")) 

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

# 10. What can you press if your program is stuck in an infinite loop?
# Close the program or press ctrl + c 

# 11. What is the difference between break and continue?
# break immediately exits the loop completely while continue skips the current iteration and moves to the next one.
for i in range(5):
    if i == 3:
        break  
    print(i)

for i in range(5):
    if i == 4:
        continue  
    print(i)



#  12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

for i in range(10):
    print(i)

for i in range(0, 10):
    print(i)

for i in range(0, 10, 1):
    print(i)


# 13. Write a short program that prints the numbers 1 to 10 using a for loop.
#  Then write an equivalent program that prints the numbers 1 to 10 using a while loop

# Using a for loop
for i in range(1, 11): 
    print(i)

# Using a while loop

i = 1  
while i <= 10:  
    print(i)
    i += 1  
