# *args
# def doSum(*x):
#     sum = 0
#     for n in x:
#         sum += n
#     print("Sum is:",sum)


# doSum()
# doSum(6)
# doSum(4,5)
# doSum(5,6,7)
# doSum(4,5,3,6,9,1)
# doSum(9,5,7,2,6,7,2,4)


# **kwargs - keyword arguments
def person(**details):
    print(details)


person(id=101)
person(id=102, name="Ram")
person(name="John", city="Mexico", salary=450000)
