# If Statements
# executes certain blocks of code dependign on the conditions
# if/conditional statements

# I wake up 
# if I'm hungry
#     I eat breakfast

# I leave my house:
# if it's cloudy 
#     I bring an umbrella
# otherwise
#     I bring sundglasses

# Im at a restaurant
# if I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spagetti & meatballs
# otherwise 
#     I order a salad

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:   
    print("You are not a male and not tall.")

# comparisons
def max_num(num1, num2, num3):
    # checking comparisons if the condition meets the statement
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3

print(max_num(312, 4, 5))