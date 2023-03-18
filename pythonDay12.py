#                                                   Day: 12
#                                           Chapter 21: Python Scope
#Local scope

def mylocal():
    x = 10                  #Local scope
    print(x)
mylocal()
#print(x)     # will through an error

#Function inside funciton
def func1():
    bhojan = "Aloo-puri"
    def func2():
        samaye = "kal subha 7 baje"
        print(bhojan, "-", samaye)
    func2()   # function 2 called inside function 1
func1()

#Global variable
bhandara = "Aloo-puri"
samaye = "- kal subha 8 bje"

def func():
    print(bhandara, samaye)
func()

#naming variable
def khana():
    samaye = "kal subha 11 bje"    # local variable
    print(bhandara, samaye)
khana()
print(bhandara, samaye)

#global keyword

arti = "kal subha 7 bje"
print(arti)
def ghar():
    #arti = "kal subha 8 bje"  #through error coz we cannot change global variable by local
    global arti
    arti = "kal subha 8 bje"
ghar()
print(arti)
