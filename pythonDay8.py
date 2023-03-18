#                                               Day 8
#                               Chapter 13: Funcitons and docstring

#def func1():                            #definition of function
    #print("You are in function 1")      # Function statement
                                        #this function is default with 0 parameter & arguments
#func1()                                 #function called

#def func2(a):                            #function with only one parameter
    #print("now you are in function 2")
    #print("You answere after multiply by 10: ", a * 10)
#print("Enter you number: ")
#a = int(input())
#func2(a)

#def func3(x, y):
    #print("Now you are in function 3")
    #print("Sum = ", x + y)

#print("Enter your first number : ", end= ""),
#x = int(input())
#print("Enter your second number : ", end= ""),
#y = int(input())

#func3(x, y)

# if you dont know the number of arguments to be passed in the funciton

def func4(*num):
    print("Your first number: ", p)
    print("Your second number: ", q)

    r = p + q
    k = r / 2
    print("Average is: ", k)
print("enter your first number: ",  end= ""),
p = int(input())
q = int(input())
(func4(p, q))

