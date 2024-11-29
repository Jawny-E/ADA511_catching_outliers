import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

sample = pd.read_csv("datasets/sample1.csv", index_col=0)
questions = pd.read_csv("datasets/questions1.csv", index_col=0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

# questions.loc[0, 'Diffuculty'] # get the data at index 0 in column 'Difficulty'

# find mean prob of getting all those questions right. Need to find what it should have been? Or is that what we do?
def findMeanProb(player):
    sum = 0
    count = 0
    for i in range(0,10):
        prob = round(sigmoid(sample.loc[player, 'Skill'] - questions.loc[i, 'Diffuculty']), 2) #probability of answering a question correctly
        if (questions.loc[i, f'S{player}'] == 1): # not relevant if they answer incorrectly - not cheating
            sum += prob
            count += 1
    print(count)
    return round(sum/count, 2)

def getCorrectGuesses(player):
    n = 0
    for i in range(0,10):
        if(sample.loc[player, f'S{i}'] == 1):
            n += 1
    return n

def findProbOfResultGivenSkill():
    min = 1
    cheater = 0
    for i in range(10):
        wins = getCorrectGuesses(i)
        fails = 10 - wins
        skill = sample.loc[i, 'Skill']
        p = 1 - sigmoid(skill)
        cp = binom.cdf(fails, 10, p)
        if cp < min:
            min = cp
            cheater = i
        print(f'{i}: {p} fails: {fails} {cp}')
    return cheater

print(findProbOfResultGivenSkill())

# sjekk hvor stor sannsynlighet det var for det eller mer
# print(binom.cdf(1000 - win, 1000, 1 - sigmoid(-0.5)))

# calculate binomial probability (k or fewer out of n, given p)
#print(binom.cdf(k=0, n=5, p=sigmoid(3)))

# chance of exactly k out of n given p
#print(binom.pmf(k=13, n=12, p=0.6))

"""
for i in range(10):
    print(findMeanProb(i))

for i in range(0,10):
    print(round(findMeanProb(i)/1000, 2))

OK. Case. Feks. 
Cheater har skill på 2.8. Og får en snitt sannsynlighet på 0.85. Men hva skulle det vært om han ikke juksa? :D
- gjennomsnitt sannsynlighet for alt rett gitt sigmoid?

kanskje det skal være "hva er sannsynligheten for n rette?"
Eller om antall rette passer med gj.snitt sannsynlighet?
Mest sannsynlig antall rette gitt skill og difficulties.........
"""