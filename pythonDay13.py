#                                                   Day 13
#                               Chapter: 22 Recursion vs iterative method
print("\t\t\t\t\t\t\t\t\t\t\t\nFactorial of number with both iterative and recusive method\n")

#With Iterative method
def fac_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

print("Enter the number: ", end="")
x = int(input())
print(fac_iterative(x))

#With Recursion method

def fac_recursion(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m * fac_recursion(m-1)

print("Enter the number: ", end=""),
y = int(input())
print(fac_recursion(y))

#Quize: fibonacci series

a = 0
b = 1
def fibonaci(n):
    if n <= 0:
        print("enter a positive integer")
    elif n == 1:
        print("Fibonacci series upto", n, ":" )
        print(a)
    elif n == 2:
        print("Fibonacci series upto", n, ":")
        print(a,b)
    else:
        print("Fibonacci series upto", n, ": ", end="")
        z = 0
        a = 0
        b = 1
        while z < n:
            print(a, " ", end="")
            fib = a + b
            a = b
            b = fib
            z += 1


print("enter the length of series: ", end=""),
m = int(input())
fibonaci(m)