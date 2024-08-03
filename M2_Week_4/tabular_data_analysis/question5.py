# Question 5
import numpy as np
import pandas as pd
from compute_correlation_cofficient import compute_correlation_cofficient

data = pd.read_csv ("advertising.csv")
x = data ["TV"]
y = data ["Radio"]

corr_xy = compute_correlation_cofficient(x , y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

# Answer: B