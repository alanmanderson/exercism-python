import random
from math import floor

class Character:
    def __init__(self):
        self.strength = generateAttribute()
        self.dexterity = generateAttribute()
        self.constitution = generateAttribute()
        self.intelligence = generateAttribute()
        self.wisdom = generateAttribute()
        self.charisma = generateAttribute()
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        ability = random.randint(1,6)
        if ability == 1: return self.strength
        if ability == 2: return self.dexterity
        if ability == 3: return self.constitution
        if ability == 4: return self.intelligence
        if ability == 5: return self.wisdom
        if ability == 6: return self.charisma

def generateAttribute():
    dice = []
    for i in range(4):
        dice.append(random.randint(1,6))
    dice.sort(reverse = True)
    dice.pop()
    print(dice)
    return sum(dice)

def modifier(constitution):
    constitution -= 10
    constitution /= 2
    return floor(constitution)
