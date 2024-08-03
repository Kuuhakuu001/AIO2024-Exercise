# Question 5
import numpy as np
import pandas as pd

def compute_correlation_cofficient (X , Y ):
    N = len(X)
    numerator = 0
    denominator = 0
    numerator = N * np.sum(X * Y) - np.sum(X) * np.sum(Y)
    denominator = np.sqrt(N * np.sum(X**2) - np.sum(X)**2) * np.sqrt(N * np.sum(Y**2) - np.sum(Y)**2)

    return np.round(numerator / denominator , 2)


data = pd.read_csv ("advertising.csv")

x = data ["TV"]
y = data ["Radio"]

corr_xy = compute_correlation_cofficient (x , y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

# Answer: B