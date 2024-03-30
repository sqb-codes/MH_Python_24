"""nested function - function inside a function"""

def outer():
    print("Outer function called...")
    def inner():
        print("Inner function called...")

    # inner()
    return inner

# print(outer())
innerFunc = outer()
innerFunc()
