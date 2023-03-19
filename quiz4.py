#                                               Quize 4
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to lucky number Lotry\n")
luck  = 0
while(luck <= 100 or luck >= 120 ):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter you lucky number: ", end = ""),
    luck = int(input())
    if luck <= 100 or luck >= 120:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease try again!\n")
else:
    print("\t\t\t\t\t\t\t\t\t\t\t\tCongratulations you are our lucky customer")

