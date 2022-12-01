import random

def roll(maxNum):
    return random.randrange(1, maxNum+1)

def shoot(numDice, maxValue):
    pass

def round():
    pass

tests = 10

for _ in range(tests):
    print(roll(10))