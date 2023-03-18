#                                       Chapter: 9 Sets and its functions
myset = {""} #empty set
print(myset)
print(type(myset))
set1 = {"oranges", "banana", "apple", "grapes", "mango"}   #set string items
set2 = {1,2,3,4,5,6,7,8,9,0}                               #set int items
set3 = {True, False}                                       #set boolean functions

print(len(set1))    #give length of the set
print(type(set2))   #give the type
set4 = set(("apple", 1,"oranges"))  #set constructor

print(set1)      #set is unodered so it will print items in random order
print(set2)      #set is unodered so it will print items in random order
print(set3)      #set is unodered so it will print items in random order

#funtions in set
#Access set items: canno access by index or key  we use for loop here
for x in set2:
    print(x)

#check is the item is present of not
#print("banana" in set1)
#print(("cherry" in set1))

#add an item to set
set1.add("cherry")      #by using add() function
print(set1)

set4 = {"cherry","pineapple", "dragon fruit", "guava"}
set1.update(set4)
print(set1)             #it update set 1 with the items of set 4

#add any itereable , it does not need to be set to add in another set

list1 = ["potato", "carrot", "chilli", "lemon"]
set1.update(list1)

print(set1)     #list items are added to set1

#Remove items from set

set1.remove("potato")
print(set1)     #it will remove the item but if it is not available in set then raise an error

#set1.remove("pencil") #throw error like: keyerror
set1.discard("carrot")  #it also remove but never throw error if item not available
print(set1)
set1.discard("pen") # no error

#set1.pop()
#print(set1) #it will also remove but the last item and we dont know which is the last item in the set

set5 = {"pen", "pencil", "scale", "eraser"}

set5.clear() #it will clear the set and make it empty
print(set5)

#set6 = {"books", "registers", "copy", "covers", "guides","question papers"}
#del set6
#print(set6)     #it will delete the set from the output and give error like not found

#python joints set
#two lady from same house come to buy vegetables
lady1 = {"potato", "lemon", "mint", "onion", "chilli","carrot", "cabbage", "broccoli", "capsicum", "radish", "brinjal"}
lady2 = {"potato", "onion", "ladyfinger", "tomato", "cauliflower", "brinjal", "radish","pumpkin", "broccoli"}
#union : all item in new set |  update insert one set item to another
#shopkeeper make union of vegetable in on beg

beg1 = lady1.union(lady2)

print("union eg:\t", beg1)  #all items in a single set

#keep only the duplicated  | shopkeeper put simillar vegetables in single beg
#which vegetables are come in the beg
lady1.intersection_update(lady2) #put simillar vegetables in lady 1 beg
print("intersection in lady 1 beg:\t", lady1)

#ladies dont bring beg shopkeer put the vegetables in a beg
beg2 = lady1.intersection(lady2)
print("intersection in shopkeepers beg:\t", beg2)

#keep all but not duplicates
#shopkeeper put different vegetables in lady 1 beg
lady2.symmetric_difference_update(lady1)
print("different vegetables in lady 2 beg", lady2) #remove common in both

#lady 2 forget to bring beg so shopkeeper give them a beg for differet vegestable
beg3 = lady2.symmetric_difference(lady1)
print("the vegetables in shopkeeper beg 3", beg3)  # remove which is common for lady1 item but print for lady 2

#to check whether two set have intersection or not  | simillar items are or not

ques = lady1.isdisjoint(lady2)
print("is intersection is there or not in lady 1 & 2: ",ques)


#subset & super set

item1 = {"pen", "pencil", "cover","books", "guide", "papers"}
item2 = {"pen", "pencil", "books"}

sub = item1.issubset(item2)
print("is item1 is subset of item 2",sub)

sub1 = item2.issubset(item1)
print("is item2 is subset of item 1",sub1)

sub3 = item1.issuperset(item2)
print("is item1 is superset of item 2",sub)

sub4 = item2.issuperset(item1)
print("is item2 is superset of item 1",sub1)












