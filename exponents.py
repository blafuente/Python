# Exponents
# writing a function to perform an exponent operation

print(2**3)
#the exponent function will perform the same opeartion as above
base_num = int(input("Enter a number: "))
pow_num = int(input("Enter a number to raise to: "))


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)

raise_to_power(base_num, pow_num)
