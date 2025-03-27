# import os
# print(os.path.join('usr','bin','spam'))

# myFiles = ['accounts..txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users', filename))


# checking your current working directory
# import os 
# print(os.getcwd())

#absolute vs relative paths

# creating new folders with os.makedirs()
# import os
# print(os.makedirs('C:\\Users\\robia\\OneDrive\\desktop\\python\\creating'))

#the os.path 
# baconFile = open('bacon.txt', 'w')
# baconFile.write('Hello world!\n')
# baconFile.close()
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable')
# baconFile.close()
# baconFile = open('bacon.txt')
# content = baconFile.read()
# baconFile.close()
# print(content)

# saving variables with the shelve module 
# import shelve
# shelfFile =  shelve.open('mydata')
# cats = ['zophie', 'pooka', 'simon']
# shelfFile['cats'] = cats
# shelfFile.close()
# print(cats)

# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

# # saving variables with the pprint.pformat
# import os
# print(os.getcwd())

# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

# import list.py

# generating random quiz 
# create 35 different quizzez
# create 50 multiple-choice questions for each quiz, radnom order
# Provide the correct answer and three random wrong answers for each question, in random order
# write the quizzes to 35 text files.
# write the answer keys to 35 text File

# this means the code will need to do the following:
# store the states and their capitals in a dictionary.
# call open(), write(), and close() for the quiz and answer key text files.
# use random.shuffle() to randomize the order of the questions and multiple-choice options

# step 1: store the quiz data in the dictionary

# randomQuizGenerator.py - creates quizzes with questions and answers in random order, along with the answer key.
# import random

# capitals = {
#             'Alabama':'Montgomery ',
#             'Alaska':'Juneau', 
#             'Arizona':'Phoenix', 
#             'Arkansas':'Little Rock', 
#             'California':'Sacremento', 
#             'New york':'Lincoln', 
#             'Maryland':'Jefferson city', 
#             'carson city':'topaka', 
#             'augusta':'little rock', 
#             'dover':'florida', 
#             'iowa':'maine', 
#             'califonia':'helena', 
#             'siant paul':'new mexico', 
#             ' oregon':'salem'
#             }

# # generate 14 quiz files
# for quizNum in range (14):
#     # TODO0: create the quiz and answer key files
#     # TODO0: write out the header for the quiz
#     # TODO0: shuffle the order of the states.
#     # TODO0: loop through all 50 states, making a question for each


# # step 2: create the quiz file and shuffle the question order
# # ! python 3
# # randomQuizGenerator.py - creates quizzes with questins and answer in random order, along with the answer key

# # --snip--

#     for quizNum in range(14):
#         #create the quiz and the answer key files
#         quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
#         answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

#         #write out the header for the quiz.
#         quizFile.write('Name:\n\nPeriod:\n\n')
#         quizFile.write(('' * 20) + 'state capitals quiz (form%s)' % (quizNum + 1))
#         quizFile.write('\n\n')

#     # shuffle the order of the state 
#     states = list(capitals.keys())
#     random.shuffle(states)

#     # TODO0: loop through all 15 states, making a question for each


# # step 3: create the answer optin

# #! python3
# # randomQuizGenerator.py - creates quizzes with questions and answer in random order, along with the answer key.

# # --snip--

# # loop through all 50 states, making a question for each.
# for questionNum in range(14):
#     # get right and wrong answers.
#     correctAnswer = capitals[states[questionNum]]
#     wrongAnswers = list(capitals.values())
#     del wrongAnswers[wrongAnswers.index(correctAnswer)]
#     wrongAnswers = random.sample(wrongAnswers, 3) 
#     answerOptions = wrongAnswers + [correctAnswer]        
#     random.shuffle(answerOptions)          

# # write content to the quiz and answer key files

# # ! python 3
# # randmQuizGenetor.py-creates quizzes with questions andanswer in random order, along side with the answer KeyboardInterrupt

# # --snip--
# # loop through all 15 states, makinga question for each.
# for questionNum in range(14):
#     # --snip--

#     #write the question and the answer options to the quiz file.
#     quizFile.write('%s. what is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
#     for i in range (4):
#         quizFile.write('        %s. %s\n' % ('ABCD'[i], answerOptions[i]))
#     quizFile.write('\n')

#     #write the answer key to a file.
#     answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
#         answerOptions.index(correctAnswer)]))
    # quizFile.close()
    # answerKeyFile.close()