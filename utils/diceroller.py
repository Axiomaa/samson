import random
import re

def dice_roll(dice_value):
    dice_amount, dice_type, bonus = split_roll(dice_value)

    # List to store the result of each dice roll
    rolls = []

    # Roll the dice and store the results
    for _ in range(dice_amount):
        roll_result = random.randint(1, dice_type)
        rolls.append(roll_result)

    # Calculate the total result including bonus
    total_result = sum(rolls) + bonus

    return total_result, rolls

def split_roll(dice_value):
    # Use regular expression to split the input string
    match = re.match(r'(\d*)d(\d+)([+-]\d+)?', dice_value)

    if not match:
        raise ValueError("Invalid input format")

    # Extract the components of the roll
    dice_amount = int(match.group(1) or '1')
    dice_type = int(match.group(2))
    bonus = int(match.group(3) or '0')

    return dice_amount, dice_type, bonus
