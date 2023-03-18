#                                                   Day 10
#                               Chapter: 16  Open, Read and Readline in file

#Creation of a new file with python
#f = open("Bhojan bhandar.txt", "x")

#Open a file * using r is not necessary as read and write are default methods
# f = open("Bhojan bhandar.txt", "r")
# print(f.read())
# f.close()     #close a file

#If you want to read some words of the file
# f = open("Bhojan bhandar.txt", "r")
# print(f.read(50))     #characters
# f.close()

#If you want to read the lines from the file
# f = open("Bhojan bhandar.txt")
# print(f.readline())      # the number of times this line is used the number of lines from the file is printed
# print(f.readline())      #second time second line  - nothing shown coz the is a blank line in the file
# print(f.readline())      #it add additional new line
# f.close()

# Readlines: print a list containing the data of file

# f = open("Bhojan bhandar.txt")
# print(f.readlines())
# f.close()

#                                       Chapter: 17 Writting and appending a file
#f = open("Mithai.txt", "x")    # created a different file for write

#write clear all the data of the file and add the new one

# f = open("Mithai.txt", "w")
# f.write("Hmari dukan 1 mahine k liye band rahegi")
#f.close()

#Adding lines in file without deleting the data

# f = open("Bhojan bhandar.txt", "a")
# f.write("Order dene k lie sampark karein 91934298323")
# f.close()

#Handle read and write at the same time
# f = open("Mithai.txt", "r+")
# print(f.read())
# f.write("\nDhanyawaad")       #Now it didn't erase the data. Add the line in the end of the file
# f.close()