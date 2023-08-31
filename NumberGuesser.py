guess = 50
playState = True
guessChange = 25

print('This is a number guessing game welcome!')
print('Choose a number between 1 and 100 but dont tell me!')

x = 0

while playState:
    print(f'Is your number (greater) than, (less) than or (equal) to {guess}')
    guessCorrectness = input()
    if guessCorrectness == "greater":
        guess = guess + guessChange
    if guessCorrectness == "less":
        guess = guess + guessChange
    if guessCorrectness == "equal":
        playState = False
        print(f'YAY! I guessed your number {guess}')
        
    guessChange = guessChange//2
    if guessChange <= 0:
        guessChange = 1
    x = x = 1