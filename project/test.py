import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

sample = pd.read_csv("datasets/sample1.csv", index_col=0)
questions = pd.read_csv("datasets/questions1.csv", index_col=0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

difficulty = (questions.loc[0, 'Diffuculty']) # get the data at index 0 in column 'Difficulty'

sum = 0
j = 0
for i in range(0,100):
    prob = round(sigmoid(sample.loc[j, 'Skill'] - questions.loc[i, 'Diffuculty']), 2) #probability of answering a question correctly
    if (questions.loc[i, f'S{j}'] == 0):
        prob = round(1 - prob, 2)
    # print(f'{prob}, {questions.loc[i, f'S{j}']}') #print probability and answers
    sum += prob

# print(round(sum/100, 2))

def findMeanProb(player):
    sum = 0
    for i in range(0,1000):
        prob = round(sigmoid(sample.loc[player, 'Skill'] - questions.loc[i, 'Diffuculty']), 2) #probability of answering a question correctly
        if (questions.loc[i, f'S{player}'] == 0):
            prob = round(1 - prob, 2)
        sum += prob
    return sum

for i in range(0,10):
    print(round(findMeanProb(i)/1000, 2))


"""
OK. Case. Feks. 
Cheater har skill på 2.8. Og får en snitt sannsynlighet på 0.85. Men hva skulle det vært om han ikke juksa? :D
- gjennomsnitt sannsynlighet for alt rett gitt sigmoid?

kanskje det skal være "hva er sannsynligheten for n rette?"
Eller om antall rette passer med gj.snitt sannsynlighet?
Mest sannsynlig antall rette gitt skill og difficulties.........
"""

