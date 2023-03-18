                                                    # Day 16
                                    # Chapter 27: Generating a random string

import random
import string           # Common string operator
import math
# Using random.choice()

#creating a random sting generator

# print("enter the length of the string: ", end=""),
# length = int(input())
# rand = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))  #it include both upper and lower case character + digits
# print("\n string is: \t", str(rand))

# methods used in string
# a = ''.join(random.choice(string.ascii_letters) for x in range(length))            #string.ascii_letters with this it will give a length of the total letters so use for
# print("Upper + lower case: ", a)
#
# b = ''.join(random.choice(string.ascii_lowercase) for x in range(length))
# print("Only lower case", b)
#
# c = ''.join(random.choice(string.ascii_uppercase) for x in range(length))
# print("Only upper case: ", c)
#
# d = ''.join(random.choice(string.digits) for x in range(length))
# print("Only digits: ", d)
#
# e = ''.join(random.choice(string.punctuation) for x in range(length))
# print("Only punctuation: ", e)

#Random string with specified characters
#
# def long(l):
#     st = "GOPALNMOPQRSTUVEX"
#     result = ''.join(random.choice(st) for x in range(l))
#     return result
#
# print("String of specified char: ", long(length))

#String without repeatative character

# def long_re(l1):
#     alpha = string.ascii_lowercase
#     result = ''.join((random.sample(alpha, l1)))
#     return result
# print("No repeatative char str: ", long_re(length))

# generating a string which have limited given digit and characters
# def randst( a, b):
#     str1 = ''.join(random.choice(string.ascii_letters) for x in range(a))
#     str2 = ''.join(random.choice(string.digits) for x in range(b))
#     list1 = list(str1 + str2)       # convert string to  list
#     random.shuffle(list1)    # shuffle the list
#     final_str = str(list1)
#     return final_str
#
# x = int(input("Enter the count of characters: "))
# y = int(input("Enter the count of digits: "))
#
# print("Your string is: ", randst(x, y))


# Chapter: 28 F-string and string formating
# string formating
me = "Gopal"
a = 20

# b = "My name is %s and i'm  year old" "%me #%a
# print(b)

# do only 1
# c = "My name is {1} and i'm {0} year old "
# d = c.format(me, a)
# print(d)

#f-string

e = f"My name is {me} and i'm {a} year old"
print(e)
