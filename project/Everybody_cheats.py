# Some messing around
import pandas as pd
import numpy as np

students = pd.read_csv("datasets/sample1.csv", index_col=0)
questions = pd.read_csv("datasets/questions1.csv", index_col=0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def get_cheater_likelihood(answer, skill, difficulty):
    """Compute likelihood if the player is the cheater (50% chance to answer correctly)."""
    p_right_cheater = 0.5 * sigmoid(skill - difficulty) + 0.5
    p_wrong_cheater = 1 - p_right_cheater
    return p_right_cheater if answer == 1 else p_wrong_cheater

def get_normal_likelihood(answer, skill, difficulty):
    """Compute likelihood for normal players based on skill and difficulty."""
    p_right_normal = sigmoid(skill - difficulty)
    p_wrong_normal = 1 - p_right_normal
    return p_right_normal if answer == 1 else p_wrong_normal
    
def compute_likelihood_for_all_students():
    """Compute the likelihood of each student being the cheater."""
    likelihoods = []
    
    for index, row in students.iterrows():
        skill = row['Skill']
        student_likelihood = 1
        for column_name, value in row.iloc[2:].items():  # Skip first two columns (ID, Skill)
            col_index = students.columns.get_loc(column_name) - 2
            difficulty = questions.at[col_index, 'Difficulty']
            
            # Calculate likelihood for cheater (50% chance of being correct)
            likelihood_cheater = get_cheater_likelihood(value, skill, difficulty)
            student_likelihood *= likelihood_cheater
        
        likelihoods.append(student_likelihood)
    
    return likelihoods

# Compute likelihoods for all students
likelihoods = compute_likelihood_for_all_students()
print(likelihoods)
# Identify the student with the highest likelihood of being the cheater
cheater_index = likelihoods.index(max(likelihoods))

print(f"This method identifies index: {cheater_index} due to having the highest probability of scoring as they did if they were a cheater: {max(likelihoods)}")