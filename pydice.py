from heapq import nlargest, nsmallest
from random import randint
import re
import json

dice_regex = re.compile(r"^(\d*)d(\d*)([hmle+t-][.+-]*)?(\d*)?$")
#            'h',  # Highest Roll
#            'l',  # Lowest Roll
#            '+',  # Add to total
#            '-',  # Remove from total
#            '.+', # Add to every individual
#            '.-', # Remove from every individual
#            'e',  # Exploding dice
#            't',  # Total


def roll(user_input: str = None, json_export: bool = False):
    result = dice_regex.search(user_input)  # Searches through the user input for the roll
    repeats = int(result.group(1))  # assign the times to roll the die
    sides = int(result.group(2))  # assign the sides of the die
    modifier = []
    try:
        modifier.append(result.group(3))
        modifier.append(int(result.group(4)))
    except:
        pass
    if (int(sides) or int(repeats)) < 1:
        return "Invalid Parameter."
    if repeats and sides:  # You can set a limit on how many sides or repeats, so to avoid hangups
        if modifier[0] is not None:  # Checking for a modifier present
            rolls = []
            for i in range(repeats):
                rolls.append(randint(1, sides))
            rolls = moder(sides=sides, rolls=rolls, modifier=modifier)
            if json_export:  # Dumps all rolls to a json
                with open('rolls.json', 'w') as file:
                    json.dump(rolls, file, indent=2)
                return "Exported to json."
            else:
                return rolls
        if modifier[0] is None:
            rolls = []
            for i in range(repeats):
                rolls.append(randint(1, sides))
            if json_export:
                with open('rolls.json', 'w') as file:
                    json.dump(rolls, file, indent=2)
                return "Exported to json."
            else:
                return rolls
    else:
        return "Exceeds the roll limit."


def moder(sides: int, rolls: list, modifier: list):
    if modifier[0] == 'e':
        return explode(sides=sides, rolls=rolls) # Return exploded dice rolls along with one that were neutral
    if modifier[0] == 'h':  # Return highest
        return nlargest(modifier[1], rolls)
    if modifier[0] == 'l':  # Return lowest
        nsmallest(modifier[1], rolls)
    if modifier[0] == '+':  # Add to sum of rolls
        sum(rolls) + modifier[1]
    if modifier[0] == '-':  # Subtract from sum of rolls
        return sum(rolls) - modifier[1]
    if modifier[0] == '.-':  # Subtract from each roll
        for i in range(0, len(rolls)):
            rolls[i] = rolls[i] - modifier[1]
        return rolls
    if modifier[0] == '.+':  # Add to each roll
        for i in range(0, len(rolls)):
            rolls[i] = rolls[i] + modifier[1]
        return rolls
    if modifier[0] == 't':  # Sum of rolls
        return sum(rolls)


def explode(sides: int, rolls: list):
    for i in range(0, len(rolls)):
        counter = 0
        loop = True
        if rolls[i] == sides:
            roll_temp = rolls[i]
            while loop:
                counter += 1
                temp = randint(1, sides)
                rolls[i] += temp
                if temp != sides:
                    rolls[i] = [rolls[i], f"Exploded {counter}"]
                    loop = False
    return rolls

