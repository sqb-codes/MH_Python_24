"""Lambda Expressions"""

# def even(num):return num % 2 == 0

# Lambda Expressions
# - Anonymous function
# - Function which are not reusable
# lambda num_1, num_2 : num_1 + num_2

numbers = [3,4,6,8,9,5,5,7,98,23,45,7]

print(list(filter(lambda num : num % 2 == 0, numbers)))
print(list(filter(lambda num : num % 2 != 0, numbers)))


tempList = [30.00, 32.00, 29.55, 30.55, 33.44, 28.55, 30.12, 28.33]

print(list(map(lambda c : 1.8 * c + 32, tempList)))
print(list(map(lambda f : (f - 32) * 1.8, tempList)))
