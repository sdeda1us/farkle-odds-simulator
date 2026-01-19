import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt

class Roller():
    def __init__(self, score: int, dice: int):
        self.score = score
        self.dice = dice
        self.dice_roll = self.roll_dice()
        self.roll_score = self.score_roll()

    def roll_dice(self):
        return [random.randint(1, self.dice) for x in range(0, self.dice)]

    def score_roll(self): 
        score = 0
        roll_counts = Counter(self.dice_roll)
        val_counts = list(roll_counts.values())
        # A straight is by definition 6 unique numbers
        if len(roll_counts) == 6:
            return 1500
        # 6 of a kind is when all 6 dice have the same value
        elif len(roll_counts) == 1: 
            return 3000
        # if any roll has a value count of 5 - 5 of a kind is the only score possible
        elif 5 in val_counts:
            return 2000
        # 4 of a kind with a pair
        elif val_counts == [4, 2]:
            return 1500
        # Two triplets
        elif val_counts == [3, 3]:
            return 2500
        # 4 of a kind without pair (filtered by ordering of if statement)
        elif 4 in val_counts:
            return 1000
        # Three pair
        elif val_counts == [2, 2, 2]:
            return 1500
        # Three of a kind
        elif 3 in val_counts:
            for key, value in roll_counts.items():
                if value == 3:
                    score = key * 100
                    die_number = key
            return score
        # 100 for rolling 1s & 50 for rolling 5's
        elif (1 in self.dice_roll) | (5 in self.dice_roll ):
            if 1 in self.dice_roll:
                score = score + (100 * roll_counts[1])
            if 5 in self.dice_roll:
                score = score + (50 * roll_counts[5])
            return score
        else:
            return 0
