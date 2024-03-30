"""Module providing a return statement working"""

# def add_two_number(x,y):
#     '''Return Sum of 2 numbers'''
#     z = x + y
#     return z

# SUM = add_two_number(4,5)
# print("Sum is :",SUM)

def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    # Packing
    return z1, z2, z3, z4

# print(calc(4,6))
# Unpacking
a,b,c,d = calc(5,6)
