def even(num):
    return num % 2 == 0

def odd(num):
    return num % 2 != 0

# print(even(12))
numbers = [3,4,6,8,9,5,5,7,98,23,45,7]

# output = []
# for num in numbers:
#     if even(num):
#         output.append(num)

# print(output)

print(list(filter(even, numbers)))
print(list(filter(odd, numbers)))
