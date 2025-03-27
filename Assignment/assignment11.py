
# craete a file and add three lines of text to the file 
robiatFile = open('robiat.txt', 'w')
robiatFile.write('Hello world!\n')
robiatFile.write("It's me, Robiat\n")
robiatFile.write('I just created a new file\n')
robiatFile.close()
robiatFile = open('robiat.txt', 'a')
robiatFile.write('i am adding an additional text with the use of append')
robiatFile.close()