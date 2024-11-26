import csv
import numpy as np

numberOfPlayers = 10
numberOfQuestions = 10
chanceOfCheating = 0.5 # 
decimalPlaces = 1

# the sigmoid function - returns a number between 0 and 1. Gives the change of success
def sigmoid(x):
    return 1/(1+np.exp(-x))

# check if a question is answered correctly
def answer(x):
    return '1' if np.random.uniform(0,1) < sigmoid(x) else '0' 

def makeSample():
    # generate defined number of players with random skill-level of [-3,3]
    players = np.round(np.random.uniform(-3, 3, numberOfPlayers), decimalPlaces)

    # generate questions with difficulty [-3,3]
    questions = np.round(np.random.uniform(-3, 3, numberOfQuestions), decimalPlaces)

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

for i in range(1, 2):
    sample, cheater, questions, players = makeSample()
    
    with open(f'datasets/sample{i}.csv', mode='w', newline='') as file:
        header = ["Status"] + ["Skill"] + [f"S{j+1}" for j in range(numberOfQuestions)]
        writer = csv.writer(file)
        writer.writerow(header)
        for index, s in enumerate(sample):
            writer.writerow(['c' if index == cheater else 't', players[index], *s])
                     
    with open(f'datasets/cheater{i}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cheater])

    with open(f'datasets/questions{i}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ["Index"] + ["Diffuculty"] + [f"S{j+1}" for j in range(numberOfQuestions)]
        writer.writerow(header)
        for index, q in enumerate(questions):
            app = []
            for s in sample:
                app.append(s[index])
            writer.writerow([index, q, *app])
