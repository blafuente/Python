# Coins program
# Going to try to mimic a cash register system

# Receive an input of a Cents amount ($0.xx)
# Coin register will give back a x amount of each type of cents currency
# Q amount of Quarters
# D amount of Dimes
# N amount of Nickles
# P amount of Pennies 

# Quarter Counter
quarter_count = 0
# Dime Counter 
dime_count = 0
# Nickle Counter 
nickle_count = 0
# Penny Counter
penny_count = 0

# Given a cents a amount, check how many times each type of coin goes into the value until it reaches that amount
# ex: $0.35 = one quarter(25) + one dime(10)
# ex: $0.75 = three quarters(25) 
# ex: $0.43 = one quarter(25) + one dime(10) + one nickle(5) + three pennies(1)

input_value = int(input("Enter a cents value(0-99): "))
first_value = input_value
# print input_value

# receive cents input 
# now to check the value of how many quarters are needed
if input_value >= 25:
    quarter_count = (input_value/25) * 1
    input_value -= (quarter_count * 25)

# print quarter_count
# print input_value

# now having a remain value, check for how many Dimes
if input_value >= 10:
    dime_count = (input_value/10) * 1
    input_value -= (dime_count * 10)

# print dime_count
# print input_value

# Checking for Nickles
if input_value >= 5:
    nickle_count = (input_value/5) * 1
    input_value -= (nickle_count * 5)

# print nickle_count
# print input_value

# checking for pennies
if input_value >= 1:
    penny_count = (input_value/1) * 1
    input_value -= (penny_count * 1)

# print penny_count
# print input_value

print( "You've given me " + str(first_value) + " cents.") 
print("You'll recive " + str(quarter_count) + " quarter(s). ")
print("You'll recive " + str(dime_count) + " dime(s). ")
print("You'll recive " + str(nickle_count) + " nickle(s). ")
print("You'll recive " + str(penny_count) + " penny(ies). ")

# def centsRegister(input_value):
#     quarter_count = 0
#     dime_count = 0
#     nickle_count = 0
#     penny_count = 0
    
#     if input_value >= 25:
#         quarter_count = (input_value/25) * 1
#         input_value -= (quarter_count * 25)
#     if input_value >= 10:
#         dime_count = (input_value/10) * 1
#         input_value -= (dime_count * 10)
#     if input_value >= 5:
#         nickle_count = (input_value/5) * 1
#         input_value -= (nickle_count * 5)
#     if input_value >= 1:
#         penny_count = (input_value/1) * 1
#         input_value -= (penny_count * 1)

#     print( "You've given me " + str(first_value) + " cents.") 
#     print("You'll recive " + str(quarter_count) + " quarter(s). ")
#     print("You'll recive " + str(dime_count) + " dime(s). ")
#     print("You'll recive " + str(nickle_count) + " nickle(s). ")
#     print("You'll recive " + str(penny_count) + " penny(ies). ")

# centsRegister(input_value)