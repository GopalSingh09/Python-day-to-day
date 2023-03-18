#                                                   Day 14
#                                       Chapter: 23 Anonymous/Lambda

#lambda function
x = lambda a : a * 10
"""
this give the multiple of 10 of any number
"""
print(x(int(input("enter the number: "))))

# function with more than two argument
y = lambda a ,b: (a / b) * 100

print("Your percentage is: ", y(int(input("Enter obtained markes here: ")), int(input("Enter total marks here: "))))


#                                       Chapter: 24 Sort()in python

list = [13,213,2343,233,21,121,12,324,34,3,4]
print("List before sorted\n", list)
list.sort()                                       # this is change the entire list
print("\nList after sorted\n" ,list)

# sort in decending order

list1 = [23,43,90,432,32,13,423,42,342,34,2,34,234,2,42,34,234,7]
print("list before sorted reverse: \n", list1)
list1.sort()
print("\nlist after only sort: \n", list1)
list1.sort(reverse=True)            #reverse by default false ,so we need to give true to make it reverse
print("\nlist after sorted reverse: \n", list1)

# Sort using key

list2 = [(2,3423,423),(42,32),(2,3),(442,3,23,23,4),(24,423),(4,324,5)]

list2.sort(key= len)
print("\nlist srt using key: \n", list2)

def take2 (element):
    return element[1]
list2.sort(key=take2)
print("\nsorted with second digit value: \n", list2)


#test in sort()
#Suppose we have a list of employee informations, where each element in a dictionary with name, age , salary ,post sort according to the boss need

employee = [
    {"Name": "Gopal", "Age":20, "Salary":30000, "Post": "Data scientist"},
    {"Name": "Abhishek", "Age":21, "Salary":32000, "Post": "Web developer"},
    {"Name": "Anubhav", "Age":19, "Salary":28000, "Post": "App developer"},
    {"Name": "Dhruv", "Age":23, "Salary":35000, "Post": "Full-stack developer"},
    {"Name": "Kanhaiya", "Age":22, "Salary":30000, "Post": "Devops specialist"}
]
print("Enter with which element you want to sort: ", end=""),
choice = input()

if choice == "name" or choice == "Name":
    employee.sort(key=lambda x: x.get("Name"))
    print("Sorted list of employee: \n", employee, end="\n")

elif choice == "age" or choice == "Age":
    employee.sort(key=lambda x: x.get("Age"))
    print("Sorted list of employee: \n", employee, end="\n")

elif choice == "Salary" or choice == "salary":
    employee.sort(key=lambda x: x.get("Salary"), reverse=True)
    print("Sorted list of employee: \n", employee, end="\n")

elif choice == "post" or choice == "Post":
    employee.sort(key=lambda x: x.get("Post"))
    print("Sorted list of employee: \n", employee, end="\n")

else:
    print("Wrong choice")


#                                       Chapter: 25 Sorted()in python

num = [23,43,423,42,32,32,34,1]
sorted_num = sorted(num)
print("\nList after sorted: \n", sorted_num)
print("Original list is: ", num)

#sorting alphabets
alpha = ['e', 'a', 'i', 'o', 'u']
sorted_vowel = sorted(alpha)
print("\nSorted vowels: \n", sorted_vowel)

#printing list in reverse

reverse_num = sorted(num, reverse=True)         #by default flase
print("\nReversed list is: \n", reverse_num)

#key is same as in sort()


#test in sorted()
"""
we want to sort the list with tuple item inside it in such a way so that the student with the highest marks in the
beginning. In the case the marks are equal the younger one will come first.
items like: name marks age
"""
print("Marks from 2150\n\n")
students = [
    ("Gopal", 1798, 20),
    ("Abhishek", 1854, 21),
    ("Anubhav", 1788, 20),
    ("Kanhaiya", 1829, 22),
    ("Dhruv", 1854, 24),
    ("Ashish", 1808, 22),
    ("Mohit", 1709, 25)
]

def sheet_sorting(item):
    marks = 2150 - item[1]
    age = item[2]
    return (marks, age)

sorted_sheet = sorted(students, key=sheet_sorting)
print("Sorted marks list: \n", sorted_sheet)