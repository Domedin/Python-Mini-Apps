print('Welcome to Mad Libs')
def playMadLibs():
    print('First say one animal')
    animal1 = input()
    print('Now say one verb ending in ing')
    verb1 = input()
    print('Now say a location')
    location1 = input()
    print('Now say another location')
    location2 = input()
    print('Now say a game')
    game = input()
    print('Now say a animal')
    animal2 = input()
    print('I saw some ', animal1 , verb1, 'in a', location1,'. ')
    print('Then I went to the', location2, 'and played', game, 'with some', animal2,'s')
    print('would you like to play again yes or no')
    playAgain = input()
    if playAgain == "yes":
        playMadLibs()
playMadLibs()