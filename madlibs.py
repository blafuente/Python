# Creating a madlibs game

# create variables
color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity name: ") 

# print out the results
print("Roses are " + color)
print(pluralNoun + " are blue")
print("I love " + celebrity)

message = """
Roses are %s
%s are blue
I love %s
""" % (color,pluralNoun,celebrity)
print(message)