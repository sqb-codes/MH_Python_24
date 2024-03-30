def calc():
    x, y = 20, 15

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub


addition, subtraction = calc()
print(subtraction())

# obj = calc()
# obj.add()
# obj.sub()
