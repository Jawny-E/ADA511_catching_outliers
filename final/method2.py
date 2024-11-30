# ********************* Imports and global variables ********************* #
import pandas as pd
import numpy as np

# In this scenario we know all
students = pd.read_csv("datasets/sample1.csv", index_col=0)
questions = pd.read_csv("datasets/questions1.csv", index_col=0)
debug = False

# ********************* Functions ********************* #
# Standard Sigmoid function
# Input: a float/int between [-6, 6]
# Output: a float between [0, 1]
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Calculates the probability of getting the outcome you got
# given that you are cheating
# Input: answer[bool 0,1], skill[float -3,3], difficulty[float -3,3]
# Out: Float [0,1]
# Note: 50/50 should not be hardcoded in future
def get_cheater_likelihood(answer, skill, difficulty):
    p_right_cheater = 0.5 * sigmoid(skill - difficulty) + 0.5
    p_wrong_cheater = 1 - p_right_cheater
    if debug:
        print(f"The probability of getting a question of {difficulty} difficulty, with skill {skill} correct when cheating is: {p_right_cheater}")
    return p_right_cheater if answer == 1 else p_wrong_cheater

# Calculates the probability of getting the outcome you got
# given that you are not cheating
# Input: answer[bool 0,1], skill[float -3,3], difficulty[float -3,3]
# Out: Float [0,1]
def get_normal_likelihood(answer, skill, difficulty):
    p_right_normal = sigmoid(skill - difficulty)
    p_wrong_normal = 1 - p_right_normal
    return p_right_normal if answer == 1 else p_wrong_normal

# Iterate through all students and answers and calculate the
# propabaility of their exact results given that theyre cheating
# ... this might be computing intensive
# buuuuut the scenario limits this 
def compute_likelihood_for_cheating_all_students():

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

# Iterate through all students and answers and calculate the
# propabaility of their exact results given that theyre not cheating
# ... this might be computing intensive
# buuuuut the scenario limits this 
def compute_likelihood_for_normalcy_all_students():
    """Compute the likelihood of each student being the normal"""
    likelihoods = []
    
    for index, row in students.iterrows():
        skill = row['Skill']
        student_likelihood = 1
        for column_name, value in row.iloc[2:].items():  # Skip first two columns (ID, Skill)
            col_index = students.columns.get_loc(column_name) - 2
            difficulty = questions.at[col_index, 'Difficulty']
            
            # Calculate likelihood for cheater (50% chance of being correct)
            likelihood_normal = get_normal_likelihood(value, skill, difficulty)
            student_likelihood *= likelihood_normal
        
        likelihoods.append(student_likelihood)
    
    return likelihoods

# ********************* Main ********************* #

def main():
    # Compute likelihoods for all students
    likelihoods_cheating = compute_likelihood_for_cheating_all_students()
    likelihoods_normal = compute_likelihood_for_normalcy_all_students()

    # Compare likelihoods for each student and store the ones who are more probabily using
    # cheating to get their results than through the normal method
    cheater_likelihoods = []
    for i in range(len(likelihoods_cheating)):
        if likelihoods_cheating[i] > likelihoods_normal[i]:
            cheater_likelihoods.append((i, likelihoods_cheating[i], likelihoods_normal[i], 'Cheater'))
        else:
            cheater_likelihoods.append((i, likelihoods_cheating[i], likelihoods_normal[i], 'Normal'))

    # Print results: Each student's index, likelihood, and whether they are more likely to be a cheater or normal
    if debug:
        for result in cheater_likelihoods:
            print(f"Player {result[0]} is more likely to be a {result[3]} with a likelihood of {result[1]}")

    # Filter the cheater_likelihoods to include only those labeled as "Cheater"
    cheaters_only = [entry for entry in cheater_likelihoods if entry[3] == 'Cheater']
    cheater_indexes = [cheater[0] for cheater in cheaters_only]
    
    print(f"Method 2, identifies indexes {cheater_indexes} as more likely to have cheated than gotten their scores fairly")
    
    # ************* Employing different outlier techniques if theres more than one flagged **************

    if len(cheaters_only) > 1:
        # 1. Maximum Relative Difference
        # identify data points that significantly deviate from their expected range or group norms, even when the absolute difference might not seem large
        cheater_with_max_relative_diff = max(cheaters_only, key=lambda x: (float(x[1]) - float(x[2])) / max(float(x[1]), float(x[2])))
        print(f"Using maximum relative difference, the index is {cheater_with_max_relative_diff[0]} with a relative difference of "
            f"{(float(cheater_with_max_relative_diff[1]) - float(cheater_with_max_relative_diff[2])) / max(float(cheater_with_max_relative_diff[1]), float(cheater_with_max_relative_diff[2]))}")

        # 2. Ratio analysis evaluates the relationship between two values by calculating their ratio
        # This method emphasizes the dominance of one metric over another, highlighting cases where one probability is significantly higher or lower than expected
        cheater_with_max_ratio = max(cheaters_only, key=lambda x: float(x[1]) / float(x[2]))
        print(f"Using maximum ratio, the index is {cheater_with_max_ratio[0]} with a ratio of "
            f"{float(cheater_with_max_ratio[1]) / float(cheater_with_max_ratio[2])}")

        # 3. Z-Score
        # Measure how far a data point deviates from the mean of its group in terms of standard deviations.
        import numpy as np
        cheating_scores = np.array([float(x[1]) for x in cheaters_only])
        normal_scores = np.array([float(x[2]) for x in cheaters_only])
        z_scores = (cheating_scores - normal_scores.mean()) / normal_scores.std()
        cheater_with_max_z_score = cheaters_only[np.argmax(z_scores)]
        print(f"Using z-scores, the index is {cheater_with_max_z_score[0]} with a z-score of {z_scores[np.argmax(z_scores)]}")
        
main()