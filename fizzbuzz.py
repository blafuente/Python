# Write a short program that prints each number from 1 to 100 on a new line. 
for i in range(1,101):

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
# For each multiple of 3, print "Fizz" instead of the number. 
    elif(i%3 == 0):
        print("Fizz")
# For each multiple of 5, print "Buzz" instead of the number. 
    elif(i%5 == 0):
        print("Buzz")

    else:
        print(i)
