#                                               Python learning day 2
#                                                      chapter 5
#                                                       variable
"""
var1 = "hello world "
var2 = 4
var3 = 36.7
var4 = "Welcome to heaven"
var5 = "67 "
var6 = "89"

#to know what the variable datatype
print(type(var1))
print(type(var2))
print(type(var3))

#to add two variable
print(var1+var4)
print(var2+var3)
print(var5+var6)        #cannot add str to int/float
#to add str with int use type cast

print(var1+str(var2))

#to take input from user

print("enter you numbers")
value = input()
print("your value is ", value)

print("number after adding by 9= ", int(value)+9)
"""


#                                                    Chapter 6
#                                                string & functions
"""
mystr = "Hello welcome to heaven"
print(mystr) #print string
print(len(mystr)) #print the length of the string

#string slicing

print(mystr[0:5])
print(mystr[0:98]) #print the index given in the string but not give any error due to the string consisnt inside it.
#skipping form string


print(mystr[0:10:1]) #no skip
print(mystr[0:10:2])#skip 1 character

#type to write string
print(mystr[0:])
print(mystr[:8])
print(mystr[:])
print(mystr[::])
print(mystr[::2])

#with -ve n=index

print(mystr[-1:0])
print(mystr[-4:])
print(mystr[-6:-2])

#string fuctions
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("heaven"))
print(mystr.count("e"))
print(mystr.capitalize())
print(mystr.find("ve"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("to", "to the"))
print(mystr.encode())
"""
#                                                     chapter 7
#                                                list and list functions

"""
mylist = ["Book", "pencil","pens","covers","scale"]
print(mylist)
print(len(mylist))

#slicing

print(mylist[0:2])
print(mylist[2:6])

numlist = [3,45,7,2,72,6,6,7,4,46,6,6]
print(numlist[::-1]) #reverse the list

#some list function they change the original list
numlist.sort()
print(numlist)

numlist.reverse()
print(numlist)

numlist.append(100) #add item in the end of the list
print(numlist)

print(numlist.count(6))

"""

#tupple
mytuple = (1,5,4,3,9) #immutable
print(mytuple)

#tuple with single item
mytpl = (1)#not a tupple
mytppl = (1,) #tupple with single item
print(mytppl)

#swapping two item with traditional mathod
"""
print("entered values:\na = 10\tb = 20")
a = 10
b = 20
temp = a
a = b
b = temp
print("After swapping \na = ", a,"b = ", b)
"""

#swapping with python method
print("entered values:\na = 10\tb = 20")
a = 10
b = 20
a,b = b,a
print("After swapping \na = ", a,"b = ", b)











