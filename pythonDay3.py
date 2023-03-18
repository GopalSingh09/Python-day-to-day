#                                               Day 3
#                               chapter 8: Dictionary and its functions
#simple dictionary
dic1 = {"breakfast":"bread", "lunch":"paneer-roti","dinner":"chole", "sweet-dish":"choco"}
print(dic1)
dic2 = {"breakfast":"parathe", "lunch":"aloo","dinner":"daal", "sweet-dish":" "}
print(dic2)

#nested dictionary

dic3 = {"Gopal":{"breakfast":"milk-bread", "lunch":"paneer-roti", "dinner":"chole"},
        "himanshu":{"breakfast":"chai", "lunch":"panner", "dinner":"omlate"},
        "neetu":{"breakfast":"chai-bread", "lunch":"daal", "dinner": "aloo"}
        }
print(dic3)
#printing specific value of key
print(dic3["Gopal"]["lunch"])
print(dic3["Gopal"]["dinner"])
print(dic3["himanshu"]["breakfast"])
print(dic3["neetu"]["lunch"])

#functions of dictionary
#adding key value in dictionary

dic1["sweet-dish"] = "cake"
print(dic1)

#deleting key value pair in dictionary
#del dic2["sweet-dish"]
#rint(dic2)

#method of copy
#dic4 = dic2 #copy dic2 to dic4
#print(dic4)
#del dic4["lunch"]
#print(dic2)     #here dic4 refer to dic2 not copied thats why it deleted from dic 2

#2nd method
#dic4 = dic2.copy()     #now if we add or delete from dic4 not effect dic2

#del dic4["sweet-dish"]
#print(dic4)
#print(dic2)

#update function
#dic2.update({"sweet-dish":"ice-cream"})    #it update blank sweet dish with  ice-cream
#print(dic2)

#print only key
print(dic1.keys())

#print only values
print(dic1.values())

#remove all elements from dictionary
#dic2.clear()
#print(dic2)

#get function return specified key value
print(dic2.get("lunch"))

#pop function remove specified item
dic1.pop("sweet-dish")
print(dic1)

#popitem show last inserted item

print(dic2.popitem())

#set value
print(dic1.setdefault("fav","paneer"))
print(dic1)




