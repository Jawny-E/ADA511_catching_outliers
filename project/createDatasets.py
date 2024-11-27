import csv
import numpy as np
import matplotlib.pyplot as plt

numberOfPlayers = 10
numberOfQuestions = 100
chanceOfCheating = 0.5 # 

decimalPlaces = 1

# the sigmoid function - returns a number between 0 and 1. Gives the change of success
def sigmoid(x):
    return 1/(1+np.exp(-x))

# check if a question is answered correctly
def answer(x):
    return '1' if np.random.uniform(0,1) < sigmoid(x) else '0' 

# returns players with skill between -3 and 3, with normal distribution
def createPlayers():
    return np.round(np.random.normal(0, 1, numberOfPlayers), decimalPlaces)


# returns questions with difficulty between -3 and 3, with uniform distribution
def createQuestions():
    return np.round(np.random.normal(-3,3, numberOfQuestions), decimalPlaces)

def makeSampleWithDifficulty():

    players = createPlayers()
    questions = createQuestions()

    # choose a random cheater (index, so our players are numbered 0-99, instead of 1-100)
    cheater = np.random.randint(0, numberOfPlayers)

    # start with player[0] and use the sigmoid(S_i-Q_j) on each question and check if they answer correctly.
    sample = []
    for i, p in enumerate(players):
        s = '' #str(round(players[i], 2))
        for q in questions:
            if i == cheater and np.random.uniform(0,1) < chanceOfCheating: # checks if cheater and whether they cheat
                s += '1'
            else: 
                s += answer(p-q)
        sample.append(s)
    return sample, cheater, questions, players

def makeSampleWithoutDifficulty():
    players = createPlayers()
    cheater = np.random.randint(0, numberOfPlayers)
    sample = []
    for i, p in enumerate(players):
        s = ''
        for j in range(numberOfQuestions):
            if i == cheater and np.random.uniform(0,1) < chanceOfCheating:
                s += '1'
            else:
                s += answer(p)
        sample.append(s)
    return sample, cheater, players 

for i in range(1, 2):
    # sample, cheater, questions, players = makeSample()
    sample, cheater, players = makeSampleWithoutDifficulty()
    
    with open(f'datasets/sample{i}.csv', mode='w', newline='') as file:
        header = ["Index"] + ["Truthfulness"] + ["Skill"] + [f"S{j}" for j in range(numberOfQuestions)]
        writer = csv.writer(file)
        writer.writerow(header)
        for index, s in enumerate(sample):
            writer.writerow([index,'c' if index == cheater else 't', players[index], *s])
                     

""" # For creating csv for cheater and question difficulty
    #with open(f'datasets/cheater{i}.csv', mode='w', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow([cheater])
    
    with open(f'datasets/cheater{i}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cheater])

    with open(f'datasets/questions{i}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ["Index"] + ["Diffuculty"] + [f"S{j}" for j in range(numberOfPlayers)]
        writer.writerow(header)
        for index, q in enumerate(questions):
            app = []
            for s in sample:
                app.append(s[index])
            writer.writerow([index, q, *app])
"""
