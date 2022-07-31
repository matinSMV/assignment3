n = int(input("enter the length: "))
numbers = []
test = []

for i in range(n):
    print(i,": ")
    n = int(input())
    numbers.append(n)
    test.append(n)
    
test.sort()

if(numbers == test):
    print("Sorted!")
else:
    print("Not sorted!")