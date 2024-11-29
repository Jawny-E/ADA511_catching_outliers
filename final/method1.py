# ********************* Imports and global variables ********************* #
import numpy as np
import pandas as pd
from scipy.stats import binom

df = pd.read_csv("datasets/sample1.csv", index_col=0)
debug = False

# Get number of questions and students
questions_len = len(df.iloc[:,2:].columns)
students_len = len(df)
if debug:
    print(f"The numbers of students in the dataset are: {students_len}")
    print(f"The numbers of questions in the dataset are: {questions_len}")

# ********************* Functions ********************* #
# Standard Sigmoid function
# Input: a float/int between [-3, 3]
# Output: a float between [0, 1]
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Get the count of correct answers for a given player index
# Input: an integer
# Output: an integer
def getCorrectAnswers(student):
    row_sum = df.loc[student, df.columns[2:]].sum()
    return row_sum

# Using the cumulative binomial distribution to get the likelyhood 
# of the amount of failures we have or less
# Input: intger, integer, float in range [0,1]
# Output: float [0, 1]
def getProbabilityOfFailures(fails, question_len, p):
    cp = binom.cdf(fails, 10, p)
    if debug:
        print(f"The likelyhood of failing {fails} times or less, given {question_len} tries, and probability of failing {p} is: {cp}")
    return cp

# Finds the probability of a student scoring as well as they did or better
# Given their intelligence and scores
# Input: int student index 
# Out: Float [0,1]
def getProbOfResultGivenSkill(student):
    corrects = getCorrectAnswers(student)
    fails = questions_len - corrects
    skill = df.loc[student, 'Skill']
    p_failure = 1 - sigmoid(skill)
    cp = getProbabilityOfFailures(fails, 10, p_failure)
    return cp

def getAllStudentsProbScore():
    results = []
    for i in range(students_len):
        results.append(getProbOfResultGivenSkill(i))
    return results
# ********************* Main ********************* #


def main():
    probabilities = getAllStudentsProbScore()
    endindex = np.argmin(probabilities)
    scoreprop = probabilities[endindex]
    print(f"Method 1: reports that index: {endindex} since they had the lowest likelyhood of scoring as they did or lower with: p = {scoreprop}")

main()  
