#                                               Quize  2
# check for the eligibility of driving by age

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the Snake way drivings.\n")
print("Enter your age:")
age = int(input())
print("As per your age:")

if  age < 18:
    print("You are not eligible for drive any vehicle.")
elif age == 18:
    print("Please visit to the driving office, We cannot take decision as you are only 18.")
elif age > 18 and age < 80:
    print("You are eliligible for driving")
elif age == 80 or age > 80 and age < 100:
    print("Please come with your medical certificate for a better decision for eligibility of your driving")
elif age == 100 or age < 150:
    print("Your age is too much, You are not eligible for driving")
else:
    print("Are you immortal or mad?")


