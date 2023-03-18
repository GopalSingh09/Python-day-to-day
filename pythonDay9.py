#                                                               Day 9
                                                # Chapter 13: functions and docstring



#passing a list in a function

# def khana(food):
#     for x in food:
#         print(x)
#
# halwai_list = ["Chole", "Chawal", "Panner", "Nan", "Chap", "Puri", "Rayta", "Salad"]
# print("Khana mein ye ye rakh lenge:\n")
# khana(halwai_list)

#Return value

# def budget(x, a):
#     z = x + b
#     return z
#
# print("\nPrice of 1st item : ", end=""),
# y = int(input())
# print("Price of 2nd item : ",  end=""),
# b = int(input())
# print("Total bill : ", budget(y, b), "/-")

#Recursion in python

# Doc string in python

# def table(n):
#     """This Function gives you a table of any number you want"""
#     if num != 0:
#         i = 1
#         for y in range(10):
#             ans = num * i
#             print(ans)
#             i += 1
#     else:
#         print("We cannot give you table of 0")
#
# print("Enter the number of which table you want to know: ", end=""),
# num = int(input())
# print(table(num))
#
# print(table.__doc__)



#                                                            Chapter 14:  Exception Handling

# print("enter first number: ")
# x = int(input())
# print("enter second number: ")
# y = input()
# try:
#     print("sum is: ", x + y)
# #except NameError:                          many exceptions
#     #print("Variable not defined")
# except:
#     print("number cannot be added to a string")
#

# print("enter first number: ")
# a = int(input())
# print("enter second number: ")
# b = int(input())
# try:
#     d = a + b
# except:
#     print("something went wrong")
# else:
#     print("nothings wrong")
#     print("sum=", d)
# finally:
#     print("Finnaly code is ended")

#Raise an execption
for y in range(10):
    print("enter your number: ")
    x = int(input())
    if x < 10:
        raise Exception("Sorry number is no longer greater than 0")
    else:
        print("You are going good ")
