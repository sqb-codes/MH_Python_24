import math

num = int(input("Enter the number : "))
sqrt_num = int(math.sqrt(num))

if(num % 2 == 0 or num % 3 == 0):
    print(f"{num} is not a prime number")
    exit()

count = 0
for i in range(5, sqrt_num, 6):
    count += 1
    if num % i == 0 or num % (i + 2) == 0:
        print(f"{num} is not a prime number")
        break

else:
    print(f"{num} is a prime number")

print(f"Took {count} iterations")