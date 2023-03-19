#                                           My first python dictionary

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to my first dictionary\n")
Mydict = {"mutable":"changable",
          "immutable": "unchangeable",
          "alumni": "men and women who have completed thier studies",
          "diversity": "fact that there are many different ideas or opinios about somthings",
          "nullify": "to make a legal agreement or decision have no legal force",
          "creamer": "a powder that is added to hot drinks instead of milk or cream",
          "emulsifier": "a substance that forms or keeps an emulsion and is often added to processed foods to prevent particular parts from separating",
          "lame": "not able to walk correctly because of physical injury to or weakness in the legs or feet"}

print("Enter your word please:")
i = input()

print(i , ":" ,Mydict[i])
