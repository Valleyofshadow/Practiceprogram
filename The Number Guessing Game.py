import random


print("Welcome to the Number Guessing Game!\nI'm thinking of a number betweeen 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")

lives = 0
if dif == 'easy':
    lives = 10
elif dif == 'hard':
    lives = 5
print("lives remaining: ", lives)


key = random.randrange(0, 100)
# print (key)
def guess():
    y = int(input('Make a guess: '))
    return y
def check(attempt):
    global i
    if key == attempt:
        i = 1
        print ('You win')
    elif key > attempt:
        print ('Too low')
        hearts()
    elif key < attempt:
        print ('Too high')
        hearts()
def hearts():
    global lives
    lives -= 1
    print("lives remaining: ", lives)
    if lives == 0:
        print ('You loss')
        global i
        i = 1


i = 0 # main loop control

while i == 0:
    check(guess())


input()