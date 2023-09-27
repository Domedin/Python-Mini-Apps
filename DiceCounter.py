import random
numOfRolls = [0,0,0,0,0,0]
for x in range(0, 10):
    roll = random.randint(1, 6)
    numOfRolls[roll - 1] += 1
    print(roll)
for x in range(1, 7):
    print("You rolled " + str(x) + " " + str(numOfRolls[x - 1]) + " times")