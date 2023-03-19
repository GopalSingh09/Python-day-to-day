#                                       Exercise 3: Guesse the number

value1 = 7   #guesses 10
value2 = 87   #guesses 15
value3 = 673  #guesses 20

print("\nWelcome in the Guessing Game\n")
print("Rules for the game: ")
print("1. You have to guese the correct number in given limited try.")
print("2. You can end the game anytime by pressing 0.")
print("3. You can choose the dificulty level. Different level gives you different number of guesses. \n\n")

easy = 5
normal = 14
hard = 19

print("Which difficulty level you want to choose\n1. Easy = One digit value\n2. Normal (one digit + two digit value)\n3. Hard( one + two + three digit value)\n")
diff = int(input())

if diff == 1:
    num1 = 000
    while(easy >= 0 ):
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGuesses left: ",easy , "\n")
        easy -= 1

        print("Enter your number: ", end = ""),
        num1 = int(input())

        if num1 == 7:
            break
        elif num1 == 0:
            print("GAME OVER \nWHY NOT")
            break
        elif num1 < 7:
            print("Your number is smaller than the answere.")
        elif num1 > 7:
            print("Your number is greater than the answere.")
    else:
        print("You have used all guesses")
        print("GAME OVER")

    print("You complete the game")



elif diff == 2:
    num2 = 000
    while(normal >= 0):
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGuesses left: ", normal, "\n")
        normal -= 1

        print("Enter your number: ", end = ""),
        num2 = int(input())
        if num2 == 87:
            break
        elif num2 == 0:
            print("GAME OVER\nWHY NOT")
            break
        elif num2 < 87:
            print("Your number is smaller than the answere.")
        elif num2 > 87:
            print("Your number is greater than the answere.")
    else:
        print("You have used all guesses")
        print("GAME OVER")

    print("You complete the game")



elif diff == 3:
    num3 = 000
    while (hard >= 0):
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGuesses left: ", hard, "\n")
        hard -= 1

        print("Enter your number: ", end=""),
        num3 = int(input())
        if num3 == 673:
            break
        elif num3 == 0:
            print("GAME OVER\nWHY NOT")
            break
        elif num3 < 673:
            print("Your number is smaller than the answere.")
        elif num3 > 673:
            print("Your number is greater than the answere.")
    else:
        print("You have used all guesses")
        print("GAME OVER")

    print("You complete the game")


else:
    print("Please choose difficulty from given above!")









