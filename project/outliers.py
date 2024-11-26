# This file plots
# the distribution of total test-scores
# and number of correct answers per question
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

path1 = "datasets/sample1.csv"
path2 = "datasets/questions1.csv"
df1= pd.read_csv(path1, index_col=0)
df2 = pd.read_csv(path2, index_col=0)


## Find data from the players
# Selecting columns after Status and Skill
successes = df1.iloc[:,2:]
total_scoresS = np.zeros([len(successes.columns)], dtype=int)
for index, row in successes.iterrows():
    print(row.sum())
    total_scoresS[index] = row.sum()
print(total_scoresS)

## Find data from the questions
successes = df2.iloc[:,1:]
total_scoresQ = np.zeros([len(successes.columns)], dtype=int)
for index, row in successes.iterrows():
    print(row.sum())
    total_scoresQ[index] = row.sum()
print(total_scoresQ)

# Plotting results
fig, axs = plt.subplots(1, 2, figsize=(10,7), tight_layout=True)
fig.suptitle('Plots')

# Student Scores
num_bins = (total_scoresS.max() - total_scoresS.min())
axs[0].hist(total_scoresS, num_bins, density=1, color='green', alpha=0.7)
axs[0].set_xlabel('Student testscores total')
axs[0].set_ylabel('Amount of students [%]')

# Question Scores
num_bins = (total_scoresQ.max() - total_scoresQ.min())
axs[1].bar(df2.index, total_scoresQ, color='blue')
axs[1].set_xlabel('Question')
axs[1].set_ylabel('Amount of correct answers')


#axs[1].plot(x, -y)
plt.show()