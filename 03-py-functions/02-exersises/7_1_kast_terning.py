import random

def roll_dice(sides = 6):
    for i in range(10):
        trow = random.randint(1, sides)
        print(trow)

roll_dice()
print("------------------------------")
roll_dice(20)
