import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

path1 = "datasets/sample1.csv"
path2 = "datasets/questions1.csv"
df1= pd.read_csv(path1, index_col=0)
df2 = pd.read_csv(path2, index_col=0)


# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
fig, axs = plt.subplots(1, 2)
fig.suptitle('Vertically stacked subplots')
axs[0].hist(pd['S1'])

#axs[1].plot(x, -y)
plt.show()