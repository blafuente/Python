# Strings

# Strings are within " " marks 
print("Giraffe Academy")

# \n New Line
print("Giraffe\nAcademy")

# \ make new lines, print out quotation marks and such

# setting variables
phrase = "Giraffe Academy"
print(phrase)

# concatenation
print(phrase + " is cool")

# lower case
print(phrase.lower())

# upper case 
print(phrase.upper())

# checks if string is upper cased
print(phrase.isupper())

print(phrase.upper().isupper())

# checking length of string
print(len(phrase))

# getting individual characters from string
# use square brackets [ ]
print(phrase[0])
print(phrase[3])

# index function, tells where a spepific character is located
print(phrase.index("G"))
print(phrase.index("a"))
print(phrase.index("Acad"))
# print(phrase.index("z")) # should throw an Error because it isn't within the string

# replace
# takes 2 arguements
print(phrase.replace("Giraffe", "Elephant"))