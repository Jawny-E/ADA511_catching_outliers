import pandas as pd


path = "datasets/sample1.csv"
df= pd.read_csv(path, index_col=0)

row_index = df.index[df['Truthfulness'] == 'c'].tolist()
print(f"The actual cheater was found at index: {row_index}")