import numpy as np
import pandas as pd

sample = pd.read_csv("datasets/sample1.csv", index_col=0)
questions = pd.read_csv("datasets/questions1.csv", index_col=0)

chanceOfCheating = 0.5

# Get number of questions and students
numberOfQuestions = len(questions)
numberOfStudents = len(questions.iloc[:,1:].columns)

# ********************* Functions ********************* #

# Standard Sigmoid function
# Input: a float/int between [-6, 6]
# Output: a float between [0, 1]
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Get the actual difficulties of the questions
# Output: Array of the difficulties
def getDifficulties():
    difficulties = []
    for i in range(numberOfQuestions):
        difficulties.append(questions.loc[i, 'Diffuculty'])
    return difficulties

# Find estimated difficulties for each question
# Output: Array of difficulties for each question
def guessDifficulties():
    guessDifficulties = []
    for i in range(numberOfQuestions):
        successRate = questions.loc[i, questions.columns[1:]].sum() / numberOfStudents
        guess = round(3 - 6 * (successRate), 2) # subtract from 3 because the scale starts there, and times 6 as it goes to -3.
        guessDifficulties.append(guess)
    return guessDifficulties

# Find likelihood for the result of a player given skill and cheating/not cheating
# Inputs: an int for player number, skill, difficulties, bool for cheating
# Output: Likelihood for the result given skill and truthfulness
def findLikelihoodForSkill(student, skill, difficulties, cheating):
    likelihood = 1.0
    for i in range(numberOfQuestions):
        prob = sigmoid(skill - difficulties[i])
        probCorrect = (chanceOfCheating * 1) + ((1 - chanceOfCheating) * prob) if cheating else prob
        likelihood *= probCorrect if questions.loc[i, f'S{student}'] == 1 else (1 - probCorrect)
    return likelihood

# Sum for likelihood for either cheating or not cheating for each student
# Input: int for student, bool for cheating
def sumLikelihoodForStudent(student, difficulties, cheating):
    sumLikelihood = 0.0
    xs = (round(x * 0.1, 2) for x in range(-30, 30))
    for i in xs:
        sumLikelihood += findLikelihoodForSkill(student, i, difficulties, cheating)
    return sumLikelihood

# Get the summed probability for all student, either for cheating or not cheating
# Input: bool for cheating
# Output: Array of summed probability for each student.
def getSummedProbabilityForStudents(difficulties, cheating):
    probs = []
    for i in range(numberOfStudents):
        p = sumLikelihoodForStudent(i, difficulties, cheating)
        probs.append(p)
    return probs

# Finds the student with the maximum ratio for cheating
# Input: Difficulties of the questions
# Output: The index of the student with the highest ratio of cheating and that ratio
def getCheater(difficulties):
    probsTruth = getSummedProbabilityForStudents(difficulties, False)
    probsCheat = getSummedProbabilityForStudents(difficulties, True)
    cheater = -1
    cheaterScore = 0
    for i in range(numberOfStudents):
        if probsCheat[i] > probsTruth[i]:
            if probsTruth[i] == 0.0:
                score = float('inf')
            else: 
                score = probsCheat[i] / probsTruth[i] # ratio analysis
            if score > cheaterScore:
                cheaterScore = score
                cheater = i
    return cheater, cheaterScore

# ********************* Main ********************* #

def main():
    guessedDifficulty = guessDifficulties()
    realDifficulty = getDifficulties()

    cheaterGuessedDiffs, scoreGuessedDiffs = getCheater(guessedDifficulty)
    cheaterRealDiffs, scoreRealDiffs = getCheater(realDifficulty)

    print(f'Knowing the difficulties, and using maximum ratio, the index is {cheaterRealDiffs} with a ratio of {scoreRealDiffs}')
    print(f'Not knowing the difficulties, and using maximum ratio, the index is {cheaterGuessedDiffs} with a ratio of {scoreGuessedDiffs}')

main()