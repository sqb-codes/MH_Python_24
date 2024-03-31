def convTemp_c_to_f(c):
    return 1.8 * c + 32

def convTemp_f_to_c(f):
    return (f - 32) * 1.8

# c = 33.44
# print(convTemp(c))

tempList = [30.00, 32.00, 29.55, 30.55, 33.44, 28.55, 30.12, 28.33]
kms = [12,34,67,34,7,9,33]
ms = [234,56565,1222,78787]


# def myMap(data, func):
#     convertedList = []
#     for item in data:
#         f = round(func(item),2)
#         convertedList.append(f)

#     return convertedList

# print(myMap(tempList, convTemp_c_to_f))
# print(myMap(tempList, convTemp_f_to_c))

print(list(map(convTemp_c_to_f, tempList)))
print(list(map(convTemp_f_to_c, tempList)))


# convertedList = []
# for temp in tempList:
#     f = round(convTemp_c_to_f(temp),2)
#     convertedList.append(f)

# print(convertedList)


# convertedList = []
# for temp in tempList:
#     f = round(convTemp_f_to_c(temp),2)
#     convertedList.append(f)

# print(convertedList)
