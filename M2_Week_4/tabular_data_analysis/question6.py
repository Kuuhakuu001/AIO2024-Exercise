# Question 6
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

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_cofficient(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

# Answer: D