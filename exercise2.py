#                                           Excercise 2
#                                       A faulty calculator

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tCalculator\n")
print("You can use \t+,\t-,\t*,\t/")
print("Enter the operator you want to use:")
op = input()
if op == "+" or op == "-" or  op == "*" or op == "/":
    print("Enter your first number:")
    a = int(input())
    print("Enter your second number:")
    b = int(input())

    if op == "+":
        if a == 56 and b == 9:
            r = 75
            print("Result: ", r)
        elif a == 9 and b == 56:
            r = 75
            print("Result: ", r)
        else:
            r = a + b
            print("Result: ", r)

    elif op == "*":
        if a == 45 and b == 3:
            r = 125
            print("Result: ", r)
        elif a == 3 and b == 45:
            r = 125
            print("Result: ", r)
        else:
            r = a * b
            print("Result: ", r)

    elif op == "/":
        if a == 56 and b == 6:
            r = 8.6
            print("Result: ", r)
        else:
            r = a / b
            print("Result: ", r)

    elif op == "-":
        if a == 97 and b == 59:
            r = 42
            print("Result: ", r)
        elif a == 59 and b == 97:
            r = -42
            print("Result: ", r)
        else:
            r = a - b
            print("Result: ", r)
else:
    print("Wow that was unexpected!")