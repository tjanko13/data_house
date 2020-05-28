import random
import pandas as pd
import numpy as np

# Counting sixes
sixes = 0

# Options on a 6-sided die
dice_options = [1, 2, 3, 4, 5, 6]
roll_limit = 5000

# Iterating to simulate rolling the die 10 times
# while roll >=

# while sixes >=
for i in range(roll_limit):
    random.shuffle(dice_options)
    roll = random.choice(dice_options)
    if roll == 6:
        sixes += 1
    else:
        pass

prob_one_roll = round((sixes / roll_limit), 7)
prob_ten_rolls = round(((sixes / roll_limit) * 10), 7)
prob_ten_rolls_7_or_more = round(((sixes / roll_limit) * 10), 7)

print(sixes)
print(roll)
print(prob_one_roll)

print(f"Probability of rolling a six in 1 roll is: {prob_one_roll}.")
print(f"Probability of rolling a six in 10 roll is: {prob_ten_rolls}.")
