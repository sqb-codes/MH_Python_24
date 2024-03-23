# Positional/Required Arguments
# def add(x,y):
#     z = x + y
#     print("Sum is",z)

# add()
# add(4)
# add(5,6)

# Default Arguments
def add(x = 0, y = 0):
    z = x + y
    print("Sum is",z)


# add()
# add(5)
# add(6,8)

# Keyword Arguments
add(x = 5, y = 8)
add(x = 6)
add(y = 7, x = 0)
add(y = 9)
add(6,8)