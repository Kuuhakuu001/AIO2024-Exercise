# Question 7

import numpy as np
import pandas as pd

data = pd.read_csv("advertising.csv")
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)

# Answer: C