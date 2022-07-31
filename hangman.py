import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']


n = int(input("Levels ? (1:Easy, 2:Normal , 3:Hard)"))
if (n == 1):
    life = 15
elif (n == 2):
    life = 10
elif (n == 3):
    life = 5
    
word = random.choice(words)
p = []
for i in range(len(word)):
    p.append('_')

while life > 0:
    print(' '.join(p))
        
    if ((''.join(p)) == word):
        print("You Win *-*")
        break
    
    user_character = input()
    user_character = user_character.lower()
    
    if (user_character in word):
        print("Yes  life ")
        for i in range(len(word)):
            if (word[i] == user_character):
                p[i] = user_character        
                
    else:
        life -= 1
        print("No  life ")