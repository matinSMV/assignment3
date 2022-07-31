import random

while True:
    n = int(input("enter number:"))

    if (n > 20 or n < 0):
        print("the number have to be between 0 to 20, Please try again:")
    else:
        break

numbers = random.sample(range(0, 20), n)
print(numbers)