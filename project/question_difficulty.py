"""
   The goal of this script is to find the probability of a 
    question difficulty given the set successful answers to
    the question
    Assumptions:
    - The student skill-levels are equally distributed
    - The difficulties are in the range [-3.00 , 3.00] with 2 decimals
    - The difficulties are equally distributed, and have equal frequencies
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

amount_of_decimals = 0


index = (6*10**amount_of_decimals) + 1
print(index)

possible_difficulties = np.linspace(-3, 3, index)
frequency_difficulty = 1/index

t = np.ones(index)

# This is the base frequency distibution
plt.plot(possible_difficulties,t*frequency_difficulty)



plt.ylim(0,1)
plt.show()