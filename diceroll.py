import random
import time
random.seed(time.ctime())

def roll(diceSize):
    number = random.randrange(1, diceSize)
    print(number)
    print('roll again?')

print('Welcome to Dice Rolling')
print('What Size of Dice would you like to roll?')
playerInput = input()
playerInput = int(playerInput)
roll(playerInput)

    