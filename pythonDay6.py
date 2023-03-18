#                                                   Day 6
#                                           Chapter: 11  For loop


#list in list
"""
episodes = [["clash of super power", 88], ["frieza's boost", 89], [" power of spirit bomb", 94], ["transformed at last", 95]]
print("\nDragon ball z fav episodes list: ")
for item, number in episodes:
    print(number, item)

# functions in for loop
# loop through a string
print("\nloop through a string")
for y in "Dracula":
    print(y)

#break statement
print("\nBreak statement after print")
for p in cartoons:
    print(p)
    if p == "sponge-bob":
        break

print("\n break statement before print")
for q in cartoons:
    if q == "sponge-bob":
        break
    print(q)

#continue statement : did not print that item
print("\nContinue statement to skip an item:")
for n in cartoons:
    if n == "sponge-bob":
        continue
    print(n)

#range function
print("\nrange function:")
for num in range(7):
    print(num)
print("\n")
for num1 in range(2,10):
    print(num1)

print("\n")
for num2 in range(10,100,5):
    print(num2)

#else keyword in for loop: after finish for loop print else statement but not when use break

print("\n")
for num3 in range(6,60,6):
    print(num3)
else:
    print("this is table of 6")

print("\n")
for num4 in range(6,60,6):
    print(num4)
    if num4 == 36:
        break
else:
    print("this is table of 6")
"""
#nested for loop
cartoons = ["shinchan", "doraemon", "reyukando", "sponge-bob", "perman", "dragon ball z", "power rangers"]
rating = ["5", "6", "2", "3", "7", "1", "4"]

for x in range(len(cartoons)):
    print(cartoons[x], "Preference: ", rating[x])



