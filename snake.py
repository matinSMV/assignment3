n = int(input("snake length: "))

snake = ""

for i in range(n):
    if (i % 2 == 0):
        snake += "*"
    else:
        snake += "#"
        
print(snake)