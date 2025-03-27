#Accessing a file
# 'r' opens a file for reading
# 'w' opens a file for writing
# 'x' opnes a file for exclusive raection
# 'a' opens a file for appending content at the end of it and without truncating existing content
# 't' opens a file in text mode
# 'b' opens a file in binary mode
# '+' opens a file for updating(reading and writing r+)



#open the file in write mode
# f = open('data.txt', 'w')
# f.write ('hello')
# f.close ()
# print(f)

# f = open('data.txt', 'w')
# f.write('world')
# f.write('Robiat')
# f.close()
# print(f)


# #open the file in append mode
# f2 = open('data.txt', 'a')
# f2.write('world')
# f2.close()
# print(f2)


# #open the file in read  mode
# f = open('data.txt')
# text = f.read()
# print(text)

#open the file in append mode
# f2 = open('data.txt', 'r+')
# f2.write('worl333d  robiat')
# f2 = open('data.txt')
# text = f2.read()
# f2.close()
# print(f2)
# print(text)

# #open the file in binary mode
# f2 = open('data.txt', 'b')
# text = f2.read()
# print(text)
# f2.close()

#open the file in writeline mode
# f2 =  open('file.txt', 'w')
# f2.writelines("text")
# f2.writelines("text")
# f2.writelines("text")
# print(f2)



#File objects serve as the main interface of the pythoncode to external files on the system
#To create a file object, use the built-in open function by providing an external filenmae and a processing mode in th form of strings which is optional
#There are different modes other then read  and write in which a file canbe opened
#when an attempt is made to open a file, which does not exist in the directory in theread mode, 'file not found' error  is displayed
#Closinga file helps torelease all the resources that were associated with the file and this is achieved using the close() method.
#the different methods that can be aapplied to files are flush(), fileno(), isatty(), next(), read(), readline(size), seek(), tell(), truncate(size),
#write(str) and writelines(sequence).

# 1. open() opens a file and returns a file object

file = open('example.txt','r')
file.write('world')
file.close()
print(file)



