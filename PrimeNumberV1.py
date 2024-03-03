num = int(input("Enter the number : "))
# assume num = 17

prime = True
for i in range(2, num):
    if num % i == 0:
        # print(f"{num} is not a prime number")
        prime = False
        break
    # else:
        # print(f"{num} is a prime number")

if prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")