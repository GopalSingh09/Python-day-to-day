#                                                Astrologer's Stars

print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Astrologer's stars designs\n")
print("Enter the length of stars: ",  end=""),
n = int(input())

if n > 0:
    print("\nFormation keys:\n1. Press 1 for normal\n2. Press 0 for reverse\n")
    print("Enter the formation type:", end=""),
    formation = int(input())
    bool(formation)


    if formation == True:
        row = 1
        column = 0

        while(row <= n):
            print("")
            while(column < row):
                print("*", end="")
                column += 1
            row += 1
            column = 0
        else:
            print("\n\nStar is generated")

    elif formation == False:
        row = n
        column = row

        while(row > 0):
            print("")
            while(column > 0):
                print("*", end="")
                column -= 1
            row -= 1
            column = row
        else:
            print("\n\nStar is generated")

    else:
        print("Please enter the correct key")

else:
    print("\n\nSorry, We cannot make 0 size star")


