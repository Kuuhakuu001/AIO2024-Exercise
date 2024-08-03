# Question 9

import numpy as np
import pandas as pd
import matplotlib . pyplot as plt
import seaborn as sns

data = pd.read_csv("advertising.csv")
plt.figure(figsize =(10 ,8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()

# Answer: B