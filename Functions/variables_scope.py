# Two types of variable scope
# - Local Scope
# - Global Scope

# Global Variables
# x = 6
# y = 7

def calc():
    # x and y are local variables of calc function
    # So we cannot use x and y outside calc function
    global x, y
    x = 6
    y = 7
    z = x + y
    print("Sum is :",z)

calc()
z = x - y
print("Sub is :",z)
