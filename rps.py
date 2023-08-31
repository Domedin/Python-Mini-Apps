import random
import time
random.seed(time.ctime())
rock = "rock"
paper = "paper"
scissors = "scissors"
def game():
    playerGuess = input('Player:')
    computerGuess = random.randrange(1, 4)

    if computerGuess == 1:
        computerGuess = rock
    if computerGuess == 2:
        computerGuess = paper
    if computerGuess == 3:
        computerGuess = scissors
    print(f'Computer: {computerGuess}')

    if computerGuess == rock and playerGuess == rock:
        print('Again!')
        game()
    if computerGuess == paper and playerGuess == paper:
        print('Again!')
        game()
    if computerGuess == scissors and playerGuess == scissors:
        print('Again!')
        game()
    if computerGuess == rock and playerGuess == scissors:
        print('YAY I win')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()
    if computerGuess == paper and playerGuess == rock:
        print('YAY I win')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()
    if computerGuess == scissors and playerGuess == paper:
        print('YAY I win')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()
    if playerGuess == rock and computerGuess == scissors:
        print('Aw I lose')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()
    if playerGuess == paper and computerGuess == rock:
        print('Aw I lose')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()
    if playerGuess == scissors and computerGuess == paper:
        print('Aw I lose')
        print('again yes or no')
        playerInput = input()
        if playerInput == "yes":
            game()

print('Welcome to rock, paper, scissors!')
print('Just type rock paper, or scissors!')
game()