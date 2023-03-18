#                                                  Day 11
#                                         Chapter: 18 Deleting file

#f = open("Mahfile.txt", "x")    #first we created a new file
# f = open("Mahfile.txt", "a")
# f.write("\nThankyou for your visit")
# f.close()
# import os
#os.remove("Mahfile.txt")     # the file is deleted
#
# if os.path.exists("Mahfile.txt"):
#     os.remove("Mahfile.txt")
#     print("The file is deleted")
# else:
#     print("File you are looking for is not available")

# Delete a folder (empty folder)
# if os.path.exists("Mahfolder"):
#     os.rmdir("Mahfolder")
#     print("folder is deleted")
# else:
#     print("Folder not found")

#Chapter: 19 seek(), tell() and more in python

#f = open("Mahdoc.txt", "x")
# f = open("Mahdoc.txt", "a")
# f.write("\nThankyou for visiting the file.")
# f.close()

# f = open("Mahdoc.txt")
# print(f.tell())         #tell the postion of the file pointer
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.tell())
#
# f.seek(50)
# print("File pointer loc after seek 50= ", f.tell())
#
# f.seek(0)
# print("File pointer loc after seek 0= ", f.tell())   # reset to 0
# f.close()

#Chapter: 20 With block in file
# we can you with syntax in this we dont need to close the file it will do it automatically

# with open("Mahdoc.txt", "a") as f:
#     f.write("This file is reset")