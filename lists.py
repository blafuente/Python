# creating a list
friends = ["Des", "Jam", "Bea", "Lena"]

# You can put any kind of data type in the list/array

print(friends)

# grabbing a certain name depending on the index
print(friends[1])
 
# Access elements from back of the list
print(friends[-2])


# selecting the certain elements up to 
print(friends[1:])

# change an element
friends[1] = "Karen"
print(friends)

# lists with numbers 
lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.extend(lucky_numbers)
print(friends)

# adding individual elements to the list 
friends.append("Justin")
print(friends)

# insert takes two parameters, index and what element
friends.insert(1, "Kelly")
print(friends)

# removing elements
friends.remove("Justin")
print(friends)

# pop removes the LAST element in the list/array
friends.pop()
print(friends)

# figuring out the index of an element
print(friends.index("Bea"))

# remove everything in the list
friends.clear()
print(friends)

# counting the number of element appears in the list
friends = [ "Des", "Jam", "Bea", "Jam", "Brian"]
print(friends.count("Jam"))

# Sorting
friends.sort()
print(friends)

# reversing a list
lucky_numbers.reverse()
print(lucky_numbers)

# Copy
friends2 = friends.copy()
print(friends2)