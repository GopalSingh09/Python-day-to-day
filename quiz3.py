#                                               Quize 3

shopping = [["apple", 50], ["banana", 40], ["oranges", 150], ["watermalon", 30], ["toffee", 1], ["chocolate", 5], ["lolipop", 2], ["laddu", 10], ["biscuit", 20], ["matthi", 5], ["frooti", 10]]

for item, price in shopping:
    if str(price).isnumeric() and price > 6 and price < 50:
        print(item, "price: ", price, "\-")


# this is quize code:

list1 = ["golgappe", 3, 7, 34, 7, 57, 24, 65, 57, "potato", 23, 4, 1 ,34, 234, 24, "carrot", 23, 6, 12, "grapes", "tomato", "apple"]
for num in list1:
    if str(num).isnumeric() and num > 6:
        print("numbers are: ", num)
else:
    print("finally finished!")