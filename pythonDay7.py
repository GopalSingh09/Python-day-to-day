#                                                       Day 7
#                                                Chapter 12: While loop
i = 0           #initialized value of i
while(i<10):     #syntax of while
    print(i)    #print i
    i += 1      #incriment value of i so it will end ,if you dont give this it will never stop and turn in infinite loop

#Break statement in while loop
print("\nBreak statement in while loop, break after p = 10")
p = 0
while(p<=15):
    print(p)
    if p == 10:
        break
    p = p+2

#continue statement in while loop
print("\nContinue statement in while loop, continue after / skip p = 14")
u = 0
while(u<=16):
    u += 2
    if u == 10:
        continue
    print(u)

#Else statement in while loop
print("\nElse statement in while loop, print else statement after while complete")
j = 0
while(j<=15):
    print(j)
    j += 2
else:
    print("J is no longer lesser then 15")



