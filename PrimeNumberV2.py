num = int(input("Enter the number : "))
# assume num = 17

count = 0
# for...else
for i in range(2, num):
    count += 1
    if num % i == 0:
        print(f"{num} is not a prime number")
        break

# if for loop will be executed without break then else block will execute
# if for loop will be terminated inside if condition then else block will not execute
else:
    print(f"{num} is a prime number")

print(f"Took {count} iterations")