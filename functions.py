# functions

def say_hi():
    print("Hello User!")

say_hi()

# parameters can be passed thru the function as well 

def sayHi(name):
    print("Hello " + name)

sayHi("Brian")
sayHi("Des")

# You can pass in multiple parameters
def greeting(name, age):
    print("Hello " + name + "! You are " + age)

greeting("Brian", "30")
greeting("Des", "31") 

# Return statement within a function
# return gets information back from a function
def cube(num):
    result = num * num * num 
    return result

print(cube(3))
print(cube(4))