# skal sjekke gjennom svarene og gjette vanskelighetsgraden
# hvert spm har 100 som har svart... 
# - dersom alle svarer riktig er det jo nødvendigvis et lett spørsmål.
# - dersom alle svarer feil er det jo vanskelig.
# så se på skilllevel til hver player - kan jo egentlig "bare" se på resultat? 1-100? Men så er det jo en cheater...

# ta inn sample1.csv
# lese kolonnen og gi tilbake en vanskelighetsgrad.

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


sample = pd.read_csv('datasets/sample1.csv', header=None) # uten header=None finner den på ting sjøl 😶

guessedDifficulty = []
for i in range(0,100):
    score = sum(sample[i]) # number who got the answer correct
    guess = round((3 - score * 6 / 100), 2) # subtract from 3 because the scale starts there, and times 6 as it goes to -3. 
    guessedDifficulty.append(guess)

difficulties = [] # pd.read_csv('datasets/questions1.csv', header=None)
with open('datasets/questions1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        difficulties.append(float(*row))

min = 1
max = 0
for i in range(0,100):
    diff = difficulties[i] - guessedDifficulty[i]
    absDiff = abs(diff)
    if absDiff < min:
        min = absDiff
    if absDiff > max:
        max = absDiff
    print(f'{i}: {diff}')
print(f'min: {min} max: {max}')

print(guessedDifficulty) # nice. That works.

# okay. Got estimated difficulty. Then guess the skills of the players? 
# result from a player[i] is a row [i].
# how to calculate?
# A player has a skill ranging from -3 to 3. To likely get a question right, the player 
# should have skill greater or equal to difficulty?

def sigmoid(p, q):
    return 1/(1+np.exp(-(p-q)))

skill = -1
first = 1 - sigmoid(skill, -1.62)
sec = sigmoid(skill, -0.54)
thrd = 1 - sigmoid(skill, 0.06)
print(f'{first}, {sec}, {thrd}, {first*sec*thrd}')

xs = (x * 0.01 for x in range(-100, 100))
for i in xs:
    x = 1/(1+np.exp(-i))
    print(f'{i}: {x}')